# Referral System

A Referral System where users can register with someone's referral code to receive incentives. Incentives would be divided between the referrer and referee according to the referral code provided. Additional features include history of referral, obtaining referral codes etc. Project is built using Django Rest Framework and APIs can be accessed through either browsable api link or postman. 



### Database Structure 
![Screenshot (33)](https://user-images.githubusercontent.com/48733548/131639436-d4ffa520-e2a1-42b3-afd3-52d8bb7e320a.png)

#### NOTES:
* Share is the way in which the user wants to divide each referral incentive. (Eg: If the share value of User A is 15 then whenever a new user B uses A’s referral code, 15 out of 20 incentive credits would be given to A and 5(20-15) to B.
* Username of the user is their email address.
* Referred By in User is the referral code of the referrer.

## Some Basic Endpoints:
* Login:
  * Url : /auth/token/login
  * Request: POST 
  * Body: {“username” , “password” }

* Sign-Up:
  * Url: /auth/users/
  * Request: POST
  * Body:   Required -> {“username”,”first_name”,”last_name”,”password”}
  * Body: Additional -> {“share”,”referred_by_code”}

* Get Referral Code:
  * Url: /api/mycode
  * Request:  GET
  * Headers: 'Authorization: Token < enter token here >'

* Referral History:
  * Url: /api/referralhistory
  * Request: GET
  * Headers: 'Authorization: Token < enter token here >'

* User Details:
  * Url: /auth/users/me
  * Request: GET
  * Headers: 'Authorization: Token < enter token here >'


## Few Example APIs:

### Sign Up:

![Screenshot (30)](https://user-images.githubusercontent.com/48733548/131639548-85d4879c-f189-4d8b-9973-70b1683aced3.png)


### Get Referral Code: 
![Screenshot (31)](https://user-images.githubusercontent.com/48733548/131639603-1898de56-16cd-4749-9bef-6c009db91761.png)

### Referral History: 


![Screenshot (32)](https://user-images.githubusercontent.com/48733548/131639639-d065eef7-1d5f-4aa5-9022-c75d01f955b3.png)




## Heroku : https://ref-flow.herokuapp.com/
## Postman Collection: https://www.getpostman.com/collections/8f82e12085819eaca348


## Some Additional Features that could be implemented in future:

* Custom editable referral codes.
* Swagger for API documentation.
* Direct Referral Links.
* Multiple Referral Codes with different share values.

