import re
import glob
import sys

def collect_optic_info(lines):
    interface_list = []

    for line in lines:
        interface = {"interface": "", "optic": "", "serial": ""}
        if re.match(r'^FPC',line):
            fpc = re.findall('\d+', line)[0]
        elif re.match(r'^    PIC',line):
            pic = re.findall('\d+', line)[0]
        elif re.match(r'^  PIC',line):
            pic = re.findall('\d+', line)[0]
        elif re.match(r'^      Xcvr',line):
            xcvr = re.findall('\d+', line)[0]
            spl = line.split()
            idx = [i for i, item in enumerate(spl) if re.match("SFP.*|XFP.*|QSFP.*|UNSUPPORTED.*", item)]

            optic = spl[idx[0]]
            interface["optic"] = optic
            interface["serial"] = spl[idx[0] - 1]

            if re.match(r'.*SX.*|,*LX.*', optic):
                interface["interface"] = "ge-" + str(fpc) + "/" + str(pic) + "/" + str(xcvr)
            elif re.match(r'.*10G.*', optic):
                interface["interface"] = "xe-" + str(fpc) + "/" + str(pic) + "/" + str(xcvr)
            elif re.match(r'.*LR4.*|.*SR4.*', optic):
                interface["interface"] = "et-" + str(fpc) + "/" + str(pic) + "/" + str(xcvr)

            interface_list.append(interface)

        elif re.match(r'^    Xcvr', line):
            xcvr = re.findall('\d+', line)[0]
            spl = line.split()
            idx = [i for i, item in enumerate(spl) if re.match("SFP.*|XFP.*|QSFP.*", item)]
            optic = spl[idx[0]]
            interface["optic"] = optic
            interface["serial"] = spl[idx[0] - 1]
            if re.match(r'.*LR.*|.*SR.*', optic):
                interface["interface"] = "xe-" + str(fpc) + "/" + str(pic) + "/" + str(xcvr)
            interface_list.append(interface)
        elif not line:
            break

    return interface_list

def collect_interface_info(lines):
    idx = [i for i, item in enumerate(lines) if re.match("^Physical interface: ge|^Physical interface: xe|^Physical interface: et",item)]
    interface_list = []

    for i in idx:
        interface = {"interface": "", "status": "", "description": ""}
        interface["interface"] = lines[i].split()[2].strip(",")
        try:
            interface["status"] = lines[i].split()[8]
        except:
            try:
                interface["status"] = lines[i].split()[7]
            except:
                break
        if re.match("^  Description:", lines[i + 2]):
            interface["description"] = lines[i + 2].split()[1]
            interface_list.append(interface)
        else:
            interface["description"] = ""
            interface_list.append(interface)

    return interface_list

def fileList():
    path = "*"
    file_list = glob.glob(path)
    file_list_1 = [file for file in file_list if file.endswith(".txt")]
    return file_list_1

def main():
    # Column 출력
    print(
        'hostname'.ljust(42) +
        'Interface'.ljust(14) +
        'Status'.ljust(9) +
        'Description'.ljust(40) +
        'Optics'.ljust(20) +
        'Serial'
    )
    for filename in fileList():
        with open(filename, "r") as hfile:
            hlines = hfile.readlines()

        # OPTIC정보 병합
        interface_info = collect_interface_info(hlines)
        optic_info = collect_optic_info(hlines)

        for i in range(len(interface_info)):
            for j in range(len(optic_info)):
                if interface_info[i]["interface"] == optic_info[j]["interface"]:
                    interface_info[i].update(optic_info[j])
                    break
                else:
                    interface_info[i]["optic"] = "X"
                    interface_info[i]["serial"] = "X"

        # 출력
        for i in range(len(interface_info)):
            print(
                filename.ljust(42)+
                interface_info[i]["interface"].ljust(14)+
                interface_info[i]["status"].ljust(9)+
                interface_info[i]["description"].ljust(40)+
                interface_info[i]["optic"].ljust(20)+
                interface_info[i]["serial"]
            )

if __name__ == '__main__':
    sys.stdout = open('result.txt', 'w')
    main()