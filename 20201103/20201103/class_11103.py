#File handling

# hello = open("F:\Gopal\PythonClass\ClassCode\hello.txt")
# file = open("test.txt","r")

# print(file.readline(), end="")

# file.close()

#Context manager
# with open("test.txt","r") as file:
#     print(file.readline(), end="")


# with open("test_write.txt", "w") as f:
#     print(f.write("This is new file."))


# with open("test_write.txt", "a") as f:
#     print(f.write("\nThis is line2."))

# with open("test.txt", "r") as file:
#     with open("test_write.txt", "w") as f:
#         data = file.readline()
#         data = data + "to learn file handling."
#         f.write(data)


with open("MerchandiseData.txt", "r") as assigment:
    with open("MerchandiseData_Profit_and_Loss_Statement_Manual.txt", "w") as wf:
        wf.write("Item,UnitCostPrice,TotalCostPrice,Count,UnitSellPrice,TotalSellPrice,Profit-LossAmount")
        header = assigment.readline()
        headers = header.split(",")
        for x in range(9):
            line1 = assigment.readline()
            data = line1.split(",")

            headers[0] = data[0]
            headers[1] = float(data[1])
            headers[2] = float(data[2])
            headers[3] = float(data[3])

            UnitSellPrice = headers[3]/headers[2]
            TotalSellPrice = UnitSellPrice*headers[2]
            TotalCostPrice = headers[1]*headers[2]
            ProfitOrLoss = TotalSellPrice-TotalCostPrice

            final_list = [headers[0], str(headers[1]), str(TotalCostPrice), str(headers[2]), str(UnitSellPrice), str(TotalSellPrice), str(ProfitOrLoss)]
            final_str = "\t".join(final_list)

            wf.write(f"\n{final_str}")



    