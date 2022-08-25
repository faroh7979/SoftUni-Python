deposit_amount = float(input())
deposti_period_months=int(input())
yearly_rake = float(input())
converted_yearly_rake=yearly_rake/100
my_amount=deposit_amount + deposti_period_months * ((deposit_amount * converted_yearly_rake)/12)
print(my_amount)
