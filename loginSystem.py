class LOGIN():
  def __init__(self,name,surname,age,password):
    self.name = name
    self.surname = surname
    self.age  = age
    self.password  = password
    
  def show_info(self):  
    print(f"Name: {self.name} \nSurname: {self.surname} \nAge: {self.age} \nPassword: {self.password}")
    



print("Welcome To User Login Screen")
print("-------------------")
print(
  "1-)Sign Up"
  "\n2-)Login"
  "\n3-)Account info"
  "\n4-)Delete Account"
  "\n5-)Exit"
)

while True:
  secim = int(input("İşlem: "))
  
  if secim == 1:
    print("Sign Up ....")
    kulAd = input("Enter Your Name: ")
    kulSoy= input("Enter Your Surname: ")
    kulYas= int(input("Enter Your Age: "))
    kulSi = int(input("Enter Your Password: "))
    log = LOGIN(kulAd,kulSoy,kulYas,kulSi)
    
    kullanici = [kulAd,kulSoy,kulYas,kulSi]

  elif secim == 2:
    KulAdi = input("Enter Your Name: ")
    if KulAdi == kulAd :
      KulSoyAd = input("Enter Your Surname: ")
      if KulSoyAd == kulSoy:
        KulSifre = int(input("Enter Your Password: "))
        if KulSifre == kulSi:
          print("Logging into your account ...")
        else:
          print("Enter your password incorrectly!!")
      else:
         print("You entered your last name wrong !!")
    else:
      print("You entered your username incorrectly !!")
  elif secim == 3:
    log.show_info()
  elif secim == 4:
    kullanici.clear()
    print("Your account has been deleted :(")
  else:
    break





