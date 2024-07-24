#!/usr/bin/env python3

import requests
from colorama import Fore, Style, init

init(autoreset=True)

def get_exchange_rate(api_key, from_currency, to_currency):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_currency}"
    response = requests.get(url)
    data = response.json()
    
    if response.status_code != 200:
        print(f"{Fore.RED}❌ Failed to get the exchange rate. Please check your API key and try again.")
        return None
    
    exchange_rate = data['conversion_rates'].get(to_currency)
    if exchange_rate is None:
        print(f"{Fore.RED}❌ Currency code {to_currency} is not supported or invalid.")
    return exchange_rate

def convert_currency(amount, exchange_rate):
    return amount * exchange_rate

def list_currency_codes(api_key):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/codes"
    response = requests.get(url)
    data = response.json()
    
    if response.status_code != 200:
        print(f"{Fore.RED}❌ Failed to retrieve currency codes. Please check your API key and try again.")
        return []
    
    return data['supported_codes']

def display_banner():
    print(f"\n{Fore.MAGENTA}{Style.BRIGHT}**********************************************{Style.RESET_ALL}")
    print(f"{Fore.MAGENTA}{Style.BRIGHT}*{Fore.CYAN} 💱 Welcome to the Currency Converter 💱 {Fore.MAGENTA}{Style.BRIGHT}*")
    print(f"{Fore.MAGENTA}{Style.BRIGHT}**********************************************{Style.RESET_ALL}\n")

def display_menu():
    print(f"{Fore.CYAN}{Style.BRIGHT}Select an option:{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}1. Convert currency")
    print(f"{Fore.YELLOW}2. List currency codes")
    print(f"{Fore.YELLOW}3. Exit{Style.RESET_ALL}")
    print("")

def main():
    api_key = 'Your-Api-Key'  # Replace with your actual API key
    
    if not api_key or api_key == 'Your-Api-Key':
        print(f"{Fore.RED}❌ API key is missing or invalid. Please update the script with a valid API key.")
        return
    
    display_banner()

    while True:
        display_menu()
        choice = input(f"{Fore.CYAN}Choose an option (1/2/3): {Style.RESET_ALL}").strip()
        
        if choice == '1':
            from_currency = input(f"{Fore.CYAN}Enter the currency you want to convert from (e.g., USD): {Style.RESET_ALL}").upper()
            to_currency = input(f"{Fore.CYAN}Enter the currency you want to convert to (e.g., MYR): {Style.RESET_ALL}").upper()
            
            exchange_rate = get_exchange_rate(api_key, from_currency, to_currency)
            if exchange_rate:
                try:
                    amount_str = input(f"{Fore.CYAN}Enter the amount in {from_currency}: {Style.RESET_ALL}")
                    if amount_str.strip() == '':
                        print(f"{Fore.RED}❌ Amount cannot be empty.")
                        continue
                    amount = float(amount_str)
                    converted_amount = convert_currency(amount, exchange_rate)
                    print(f"\n{Fore.GREEN}💵 {amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}\n")
                except ValueError:
                    print(f"{Fore.RED}❌ Please enter a valid amount.")
        
        elif choice == '2':
            codes = list_currency_codes(api_key)
            if codes:
                print(f"\n{Fore.BLUE}🌍 Supported Currency Codes 🌍{Style.RESET_ALL}")
                for code in codes:
                    print(f"{Fore.YELLOW}{code[0]} - {code[1]}{Style.RESET_ALL}")
                print("")
        
        elif choice == '3':
            confirm_exit = input(f"{Fore.YELLOW}Are you sure you want to exit? (y/n): {Style.RESET_ALL}").strip().lower()
            if confirm_exit == 'y':
                print(f"{Fore.GREEN}👋 Exiting the program. Goodbye!{Style.RESET_ALL}")
                break
        
        else:
            print(f"{Fore.RED}❌ Invalid option. Please try again.")

if __name__ == "__main__":
    main()
