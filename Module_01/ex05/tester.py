from load_image import ft_load
import pimp_image

array = ft_load("landscape.jpg")

invert = pimp_image.ft_invert((array))
red = pimp_image.ft_red(array)
green = pimp_image.ft_green(array)
blue = pimp_image.ft_blue(array)
grey = pimp_image.ft_grey(array)
pimp_image.print_nd_image(invert)
pimp_image.print_nd_image(red)
pimp_image.print_nd_image(green)
pimp_image.print_nd_image(blue)
pimp_image.print_nd_image(grey)
print(pimp_image.ft_invert.__doc__)
