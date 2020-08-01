import sys

def fill(array, num_element, i, original_value, new_value):
    if i < 0 or i >= num_element:
        return
    if array[i] != original_value:
        return
    if array[i] == new_value:
        return
    else:
        array[i] = new_value
        fill(array, num_element, i - 1, original_value, new_value)
        fill(array, num_element, i + 1, original_value, new_value)
        return


    


def main():

    contents = sys.stdin.readlines()
    
    n = int(contents[0].split()[0])
    i = int(contents[0].split()[1])
    x = int(contents[0].split()[2])
    array = contents[1].split()

    for a in range(len(array)):
        array[a] = int(array[a])

    
    fill(array, n, i, array[i], x)
    array = [str(num) for num in array]
    print(" ".join(array))
    # for k in range(n):
    #     print(array[k])

if __name__ == "__main__":
    main()