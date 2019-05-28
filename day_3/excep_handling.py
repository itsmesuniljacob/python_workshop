ctr = 1
while ctr != -1:
    try:
        ctr = int(input("Enter a number (-1 to exit): "))
    except ValueError:
        print('That was not a number')
    except:
        print('Caught the exception')
    finally:
        print('Finally') #always get executed
    