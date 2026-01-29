def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

start_year = int(input("Enter the first year: "))
end_year = int(input("Enter the second year: "))

if start_year > end_year:
    start_year, end_year = end_year, start_year

leap_years = [year for year in range(start_year + 1, end_year) if is_leap(year)]

print(f"Leap years between {start_year} and {end_year}: {leap_years}")
print(f"Total count: {len(leap_years)}")

OUTPUT:-
Enter the first year: 2025
Enter the second year: 2035
Leap years between 2025 and 2035: [2028, 2032]
Total count: 2

=== Code Execution Successful ===
