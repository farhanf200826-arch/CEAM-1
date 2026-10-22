A = [
    [0,   30,  60,  90,  120],
    [20,  50,  80,  110, 140],
    [40,  70,  100, 130, 160],
    [60,  90,  120, 150, 200],
    [80,  110, 180, 220, 255]
]


def show(img):
    for i in img:
        print(i)           



def invert(img):
    c=list()
    x =0
    for i in img:
        b = list()
        for j in i:
            x=255-j
            b.append(x)
        c.append(b)
    return c


def brightness(img):
    x = int(input("enter the brightness factor:"))
    c =list()
    for i in img:
        b=list()
        for j in i:
            j=j+x
            if(j>255):
                j=255
            elif(j<0):
                j=0
            b.append(j)
        c.append(b)
    return c


def threshold(img):
    x = int(input("enter the thresholding factor:"))
    c =list()
    for i in img:
        b=list()
        for j in i:
            if j<x:
                j=0
            elif j>=x:
                j=255
            b.append(j)
        c.append(b)
    return c


def h_flip(img):
    c =list()
    for i in img:
        b =list()
        x =len(i)
        for j in range(x):
            b.append(i[x-j-1])
        c.append(b)
    return c


def v_flip(img):
    c =list()
    c = img[::-1]
    return c


def rotate(img):
    c =list()
    x =len(img)
    y = len(img[0])
    for j in range(y):
        b =list()
        for i in range(x-1,-1,-1):
            b.append(img[i][j])
        c.append(b)
    return c


def edge(img):
    c =list()
    x =len(img)
    y =len(img[0])
    for i in range(x):
        b=list()
        for j in range(y-1):
            diff = abs(img[i][j] - img[i][j+1])

            if diff>50:
                b.append(255)
            else:
                b.append(0)
            
        b.append(0)
        c.append(b)
    return c



def load_ppm():
    f = open("test.ppm", "r")
    a = f.read().split()
    f.close()

    w = int(a[1])
    h = int(a[2])

    print("Width:", w)
    print("Height:", h)
    print("Pixel values:")

    k = 4

    for i in range(h):
        for j in range(w):
            print(a[k:k+3], end=" ")
            k = k + 3
        print()




def main():

   while True:
    choice = int(input("1-INVERT,2-BRIGHTNESS,3-THRESHOLD,4-HORIZONTAL FLIP,5-VERTICAL FLIP,6-ROTATE,7-edge detection, 8-ppm ,1-exit::"))
    print("\n")

    if choice==1:
        print("The original Image is:")
        show(A)
        print("the new image is:")
        show(invert(A))

    elif choice==2:
        print("The original Image is:")
        show(A)
        print("\n")
        show(brightness(A))

    elif choice==3:
        print("The original Image is:")
        show(A)
        print("\n")
        show(threshold(A))

    elif choice==4:
        print("The original Image is:")
        show(A)
        print("the new image is:")
        show(h_flip(A))

    elif choice==5:
        print("The original Image is:")
        show(A)
        print("the new image is:")
        show(v_flip(A))

    elif choice==6:
        print("The original Image is:")
        show(A)
        print("the new image is:")
        show(rotate(A))

    elif choice ==7:
        print("The original Image is:")
        show(A)
        print("the new image is:")
        show(edge(A))

    elif choice ==8:
        load_ppm()


    elif choice==-1:
        break



       
  
main()

