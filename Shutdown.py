def shutdown(choice):
    if choice=="yes":
        return "Shuttinig down"
    elif choice=="no":
        return "Unable to shutdown "
    else:
        return "???"
choice=input("Enter condition: ")
print(shutdown(choice))