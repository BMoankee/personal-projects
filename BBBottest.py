import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

print("STARTING BOT")

# for using chrome follow this path
browser = webdriver.Chrome('"CHROMEDRIVER.EXE FILE PATH"')

# BestBuy GPU of Choice webpage
#browser.get("https://www.bestbuy.com/site/nvidia-geforce-rtx-3060-ti-8gb-gddr6-pci-express-4-0-graphics-card-steel-and-black/6439402.p?skuId=6439402")

#BestBuy Purchasable Item for referance
browser.get("https://www.bestbuy.com/site/tzumi-bytes-connector-plug-protector-2-pack-sunglasses-poop-emoji/6361993.p?skuId=6361993") 


buyButton = False

while not buyButton:

    try:
        #if this works then button is not clickable
        addToCartButton = addButton = browser.find_element_by_class_name("btn-disabled")

        #Button isn't ready then restart
        print("Button Isn't Ready Yet.")

        #Refreash the page after a delay
        time.sleep(1)
        browser.refresh()

    except:
        #add to cart is working
        addToCartButton = addButton = browser.find_element_by_class_name("btn-primary")

        #click add to cart button 
        print("Button was CLICKED!!!")
        addToCartButton.click()
        
        #Going to cart
        goToCartButton = cartButton = browser.find_element_by_class_name("cart-label")
        print("Added to CART")
        goToCartButton.click()


#fix this for checkout needed delay
        time.sleep(3)

        checkoutButton = checkButton = browser.find_element_by_class_name("btn-primary")
        print("Proceeding to CHECKOUT")
        checkoutButton.click()

        #I need to have the api log into best buy if not already logged in.

        browser.implicitly_wait(2)

        username_Textbox = browser.find_element_by_id("fld-e")
        username_Textbox.send_keys("email@mail.com")

        password_Textbox = browser.find_element_by_id("fld-p1")
        password_Textbox.send_keys("PASSWORD")

        signInButton = browser.find_element_by_class_name("btn-secondary")
        signInButton.click()
    
    # PLACE ORDER

        browser.implicitly_wait(3)
#        page = browser.find_element_by_tag_name("html")
 #       page.send_keys(Keys.END)
        browser.execute_script("window.scrollTo(0,900)")
        browser.implicitly_wait(1)

        placeOrderButton = orderButton = browser.find_element_by_css_selector("button.btn:nth-child(1)")
        placeOrderButton.click()

        time.sleep(3)

        #placeOrderButton.click()

        #time.sleep(2)

        ##placeOrderButton.click()

        print("ORDER PLACED!")

        buyButton = True