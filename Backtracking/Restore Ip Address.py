def restoreIpAddress(s):
    result = []

    def backtracking(index,parts,path):
        if parts == 4:
            if index == len(s):
                result.append(".".join(path))
            return
        
        for length in range(1,4):
            if index + length > len(s):
                break
            
            part = s[index:index+length]

            if len(part) > 1 and parts[0] == 0:
                continue

            if int(part) <= 255:
                path.append(part)

                backtracking(index + length, parts,path)

                path.pop()

    backtracking(0,0,[])
    return result 