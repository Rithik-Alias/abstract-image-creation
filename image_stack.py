from random import *
from numpy import *
from matplotlib import image, pyplot

image1 = array(image.imread("image1.jpg"))
image2 = array(image.imread("image2.jpg"))
image3 = array(image.imread("image3.jpg"))
image4 = array(image.imread("image4.jpg"))

size = 4
Stack = [0] * size
top = 0


def is_empty():
    if top == 0:
        return True
    else:
        return False


def push(image, stack):
    global top
    # top = top + 1
    if top >= size:
        print("Stackoverflow")
    else:
        stack[top] = image
        top = top + 1


def pop(stack):
    global top
    if is_empty():
        print("Stackunderflow")
    else:
        top = top - 1
        return stack[top]


def pop_index(i):
    global top
    if is_empty():
        print("Stackunderflow")
    else:
        return Stack[i - 1]


push(image1, Stack)
push(image2, Stack)
push(image3, Stack)
push(image4, Stack)
print("Displaying elements in stack in LIFO manner ")
print("Image 4 :")
poped_image = pop(Stack)
pyplot.imshow(poped_image)
pyplot.show()
print("Image 3 :")
poped_image = pop(Stack)
pyplot.imshow(poped_image)
pyplot.show()
print("Image 2 :")
poped_image = pop(Stack)
pyplot.imshow(poped_image)
pyplot.show()
print("Image 1 :")
poped_image = pop(Stack)
pyplot.imshow(poped_image)
pyplot.show()
print(f"Displaying abstract image stack that obtained from reading random n blocks from {size} images")
stack_abstract = [0] * 4
top = 0
width_newimage = min(len(image1[1]), len(image2[1]), len(image3[1]), len(image4[1]))
image = [0] * 4
image[0] = image1[:4 * 500, :3000]
image[1] = image1[:4 * 500, :3000]
image[2] = image1[:4 * 500, :3000]
image[3] = image1[:4 * 500, :3000]
for i in range(4):
    Stack.append(image1)
    Stack.append(image2)
    Stack.append(image3)
    Stack.append(image4)
    block_size = 500#randrange(500, 800)

    shuffle(Stack)
    s = 400#randrange(1000)
    print(s)
    poped_image = Stack.pop()
    image[i][:block_size, :3000] = image1[s: s + block_size, :3000]
    poped_image = Stack.pop()
    image[i][block_size: 2 * block_size, :3000] = image2[s: s + block_size, :3000]
    poped_image = Stack.pop()
    image[i][2 * block_size:3 * block_size, :3000] = image3[s: s + block_size, :3000]
    poped_image = Stack.pop()
    image[i][3 * block_size:4 * block_size, :3000] = image4[s: s + block_size, :3000]
    pyplot.imshow(image[i])
    pyplot.show()
