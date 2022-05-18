import os
os.system("pkg install -y ttyrec")
os.system("clear")
banner = """         
        <Tenshi> ┈┈┈╲╲╲╲╲╲┈┈┈┈ </Tenshi> 
                 ┈┈╱╱╲╲╲╲╲╲┈┈┈┈┈ 
                 ┈┈╱╱▏◤┃◥▕╲┈┈┈┈┈ 
                 ┈┈╰┓▏╯╰╮▕╯┈┈┈┈┈ 
                 ┈┈┈┃╭╯╰╯▕┈┈┈┈┈┈ 
                 ┈┈┈┃┊┈╭╮▕┈┈┈┈┈┈ 
                 ┈┈╱▔╲▁▁▁╱╲┈┈┈┈┈ 
                 ▔▔╲╱▔╲▉╱╲╱▔▔▔╲┈
"""
print(banner)
print("Hola soy el Profe")
input()
os.system("clear")
print(banner)
print(""" Te esnseñare a manejar la terminal como profecional\n 
                     De esta manera""")
os.system("ttyplay -s 2 ejemplo.rec")
os.system("clear")
print(banner)
print("Quieres continuar como mi alumno?")
print("""
        escribe la palabra
        [si] para conseguir premium
        [no] para salir
        """)

continuemos = input()
if continuemos == "si":
   os.system("apt install gnupg")
   os.system("clear")
   print(banner)
   print("comunicate con el Profe para conseguir premium")
   os.system("termux-open-url https://wa.me/50245472034")
   input()
   os.system("gpg premium.sh.gpg")
   os.system("bash premium.sh")
elif continuemos == "no":
    os.system("exit")




  

