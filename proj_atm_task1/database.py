#database
import mysql.connector
from mysql.connector import Error


def cre_con():
    try:
        connection = mysql.connector.connect(host="localhost",user="root",password="",database="atm_database")
        
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error while\n connecting to MySQL: {e}")
        return None

def get_balance(Acc_no):
    connection = cre_con()
    if connection:
        try:
            cursor = connection.cursor()
            qry = "SELECT amt,Acc_no FROM customer_details WHERE card_no = %s"
            cursor.execute(qry, (Acc_no,))
            result = cursor.fetchone()
        except Error as e:
            return f"Error executing query: {e}"
        finally:
            cursor.close()
            connection.close()
        
        if result:
            current_amt,Acc_no=result
            return f"Balance Form!\nYour balance is:Rs{result[0]:.2f}\nfrom Account NO.{Acc_no}"
        else:
            return "Account not found"
    else:
        return "Failed to connect to the database"


def store_deposit(card_no, amt):
    connection = cre_con()
    if connection:
        try:
            cursor = connection.cursor()
            qry = "SELECT amt,Acc_no FROM customer_details WHERE card_no = %s"
            cursor.execute(qry, (card_no,))
            result = cursor.fetchone()
            if result:
                current_amt,Acc_no=result
           
                deposit_amount = float(amt)  # Convert deposit amount to float
                qry = "UPDATE customer_details SET amt = amt + %s WHERE card_no = %s "
                cursor.execute(qry, (deposit_amount, card_no))
                connection.commit()  # Make sure to commit the transaction
                return f"Deposit successful!\nDeposited \nRs.{deposit_amount:.2f}\n to account {Acc_no}"
            else:
                return "Account not found"
        except Error as e:
            return f"Error while storing deposit in the database: {e}"
        finally:
            cursor.close()
            connection.close()

            
def store_withdraw(card_no, amt):
    connection = cre_con()
    if connection:
        try:
            cursor = connection.cursor()
            qry = "select amt,Acc_no from customer_details where card_no=%s "
            cursor.execute(qry, (card_no,))
            result = cursor.fetchone()
            if result:
                current_amt,Acc_no=result
                available_balance = float(result[0])  # Convert balance to float
                withdrawal_amount = float(amt)  # Convert withdrawal amount to float
                if available_balance >= withdrawal_amount:
                    qry = "update customer_details set amt=amt-%s where card_no=%s"
                    cursor.execute(qry, (withdrawal_amount, card_no))
                    connection.commit()  # Make sure to commit the transaction
                    return f"Withdrawal successful!\nWithdrew \nRs.{withdrawal_amount:.2f}\n from account {Acc_no}"
                else:
                    return "Insufficient balance"
            else:
                return "Account not found"
        except Error as e:
            return f"Error while storing withdrawal in the database: {e}"
        finally:
            cursor.close()
            connection.close()
    
def check_pin(card_no):
    connection = cre_con()
    if connection:
        try:
            cursor = connection.cursor()
            qry = "SELECT pin_no FROM customer_details WHERE card_no = %s"
            cursor.execute(qry, (card_no,))
            result = cursor.fetchone()
            cursor.close()
            connection.close()
            print(f"Query executed: {qry} with card_no: {card_no}")
            print(f"Query result: {result}")
            if result:
                return result[0]  # Return the pin_no from the result
            else:
                return None
        except Exception as e:
            print(f"Error while retrieving pin number: {e}")
            return None
    else:
        print("Error establishing database connection.")
        return None

'''
def list_all_cards(acc_no):
    connection = cre_con()
    if connection:
        try:
            cursor = connection.cursor()
            qry = "SELECT card_no, pin_no FROM customer_details acc_no = %s"
            cursor.execute(qry)
            result = cursor.fetchall()
            cursor.close()
            connection.close()
            for row in result:
                print(f"Card No: {row[0]}, PIN: {row[1]}")
                return row[0]
        except Exception as e:
            print(f"Error while retrieving card details: {e}")

list_all_cards()

def get_pin_for_account(acc_no):
    connection = cre_con()
    if connection:
        try:
            cursor = connection.cursor()
            qry = "SELECT pin_no FROM customer_details WHERE acc_no = %s"
            cursor.execute(qry, (acc_no,))
            result = cursor.fetchone()
            cursor.close()
            connection.close()
            if result:
                return result[0]  # Return the PIN
            else:
                print("No PIN found for the provided account number.")
                return None  # Return None if no PIN is found
        except Exception as e:
            print(f"Error while retrieving PIN: {e}")
            return None
acc_no = 111222
pin = get_pin_for_account(acc_no)
print("PIN:", pin)
'''
def get_pin(acc_no):
    connection = cre_con()
    if connection:
        try:
            cursor = connection.cursor()
            qry = "SELECT pin_no FROM customer_details WHERE card_no = %s"
            cursor.execute(qry, (acc_no,))
            results = cursor.fetchall()
            cursor.close()
            connection.close()
            if results:
                pins = [result[0] for result in results]
                return int(pins[0])  # Return a list of PINs
            else:
                print("No PINs found\nfor the provided\naccount number\nPls press OK and\nReEnter your Account NO.")
                return None  # Return None if no PINs are found
        except Exception as e:
            print(f"Error while retrieving PINs: {e}")
            return None

