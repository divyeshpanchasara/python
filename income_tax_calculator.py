print("please enter your salary ")
income=float(input())
print("total no of dependents?? ")
dependents=int(input())
stnd_dec=10000
add_ded= dependents*3000
taxable_income=income-(stnd_dec+add_ded)
tax_payable=taxable_income*0.20
print("The Income tax is ",tax_payable)
