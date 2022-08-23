# OriflamianBlogStore

REST API Application

Back-end restfull application for sharing an opinion about products.I started to create this application for present to my friend.The main idea is to helpe her in MLM buisnes. Bloggers have access only to the blog and can make posts and to write review other posts. The application has only super admin, he can creat products and chategories.Bloggers also can make orders.The application uses STRIPE payment service for charging.Only after admin approve teh order, Stripe charge the user. The project can be extended with additional functionality, like adding other users /partners/,who will use an additional discount on the price of the products and they can create a team.




## Run the app

   http://localhost:5000/

## Run the tests

Run the test suite from the tests folder.    

# REST API

The REST API app is described below.

## Register Users

### Request

`POST /register/`

    curl -X POST http://127.0.0.1:5000/register/ \     
     -H "Content-Type: application/json" \
     -d '{
    "email":"viktor@abv.bg",
    "password":"123$Qwer",
    "first_name": "Viktor",
    "last_name": "Gergov",
    "phone":"+359893111111"     
     }'

### Response

    HTTP/1.1 201 CREATED
    Date: Wed, 05 Jan 2022 09:37:55 GMT
    Status: 201 Created
    Connection: close
    Content-Type: application/json
    Content-Length: 190

    []

## Login User

### Request

`POST /login/`

    curl -X POST http://127.0.0.1:5000/login/ \     
     -H "Content-Type: application/json" \
     -d '{
    "email":"viktor@abv.cbg",
    "password":"123$Qwer"         
     }'
### Response

    HTTP/1.1 200 OK
    Date: Wed, 05 Jan 2022 09:57:03 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json    
    Content-Length: 155

    {
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjEsImV4cCI6MTY1MDAxNTQ3NSwicm9sZSI6IlVzZXJNb2RlbCJ9.PPDa32vasrEE_qEoA5kQ9kjpuBZxw427kOaf2527VrI",
    }

## Create Admin

### Request

`POST /admins/create`

    curl -X POST http://127.0.0.1:5000/admins/create \
      -H "Authorization: Bearer <admin token>"
     -H "Content-Type: application/json" \
     -d {
    "email":"superadmin@abv.bg",
    "password":"123$Qwer",
    "first_name": "violeta",
    "last_name": "kalcheva",
    "phone":"+359893527415"    
    }
### Response

    HTTP/1.1 201 CREATED
    Date: Wed, 05 Jan 2022 10:19:55 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 4

    201
    
## Login Admin

### Request

`POST /admins/login`

    curl -X POST http://127.0.0.1:5000/admins/login \     
     -H "Content-Type: application/json" \
     -d {
    "email":"superadmin@abv.bg",
    "password":"123$Qwer",       
    }
### Response

    HTTP/1.1 200 OK
    Date: Wed, 08 Aug 2022 10:29:26 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 167

    {
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjEsImV4cCI6MTY1MDAxODU2Niwicm9sZSI6IkFkbWluaXN0cmF0b3JNb2RlbCJ9.SCD4j5ya4FKk6VSpSACxKH2HGkYZ2ttEr-AEiMvmpa0"
    }
    
## Create Category

### Request

`POST /admin/category`

    curl -X POST http://127.0.0.1:5000/admin/category \     
     -H "Authorization: Bearer <admin token>"
     -H "Content-Type: application/json" \
     -d {"type": "fragrance"}
### Response

    HTTP/1.1 201 Created
    Date: Wed, 05 Jan 2022 10:54:52 GMT
    Status: 201 Created
    Connection: close
    Content-Type: application/json
    Content-Length: 197

   {
    "type": "fragrance",
    "id": 5
   }
    
    
## Create Product

### Request

`POST /admin/products`

    curl -X POST http://127.0.0.1:5000/admin/products \ 
     -H "Authorization: Bearer <admin token>"
     -H "Content-Type: application/json" \
     -d {"name": "eclat", "description": "style", "ingredients": "aroma", "how_to_use": "enjoy", "image": "/9j/decoded_photo//2Q==", "extension": "jpeg", "price": 29.99, "category_id": 5}
### Response

    HTTP/1.1 201 Created
    Date: Wed, 05 Jan 2022 10:54:52 GMT
    Status: 201 Created
    Connection: close
    Content-Type: application/json
    Content-Length: 197
    {
    "price": 29.99,
    "id": 9,
    "ingredients": "aroma",
    "image_url": "https://oriflamian-blog-store.s3.eu-central-1.amazonaws.com/bae7c569-0fd8-4211-a906-fc5bc05bb698.jpeg",
    "category_id": 5,
    "category": {
        "type": "fragrance",
        "id": 5
    },
    "how_to_use": "enjoy",
    "description": "style",
    "name": "eclat"
}
   

## Get Products

### Request

`GET /admin/products`

    curl -X POST http://127.0.0.1:5000/admin/products \ 
     -H "Authorization: Bearer <admin token>"
     -H "Content-Type: application/json" \
     
      
### Response

    HTTP/1.1 200 OK
    Date: Wed, 05 Jan 2022 10:54:52 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 197

 {
        "price": 49.99,
        "id": 1,
        "ingredients": "vitaminE",
        "image_url": "https://oriflamian-blog-store.s3.eu-central-1.amazonaws.com/d265f022-280e-4ded-a6a9-64618042ea55.jpeg",
        "category_id": 1,
        "category": {
            "type": "skin care",
            "id": 1
        },
        "how_to_use": "For best results, apply every morning",
        "description": "NovAge Brilliance Infinite Luminosity",
        "name": "day cream"
    },
    {
        "price": 49.99,
        "id": 2,
        "ingredients": "vitaminE",
        "image_url": "https://oriflamian-blog-store.s3.eu-central-1.amazonaws.com/296d0ba4-8647-49ee-943c-2f1dec604242.jpeg",
        "category_id": 1,
        "category": {
            "type": "skin care",
            "id": 1
        },
        "how_to_use": "For best results, apply every evening",
        "description": "NovAge Brilliance Infinite Luminosity",
        "name": "night cream"
    },
    {
        "price": 69.99,
        "id": 3,
        "ingredients": "Pea protein Apple powder Whole egg powder",
        "image_url": "https://oriflamian-blog-store.s3.eu-central-1.amazonaws.com/3dcaa93c-5e14-4676-881c-b8c83c1d718e.jpeg",
        "category_id": 2,
        "category": {
            "type": "wellness",
            "id": 2
        },
        "how_to_use": "replaces a meal",
        "description": "Vanilla Flavored Natural Balance Shake",
        "name": "wellness shake"
    },
    {
        "price": 69.99,
        "id": 4,
        "ingredients": "Pea protein Apple powder Whole egg powder",
        "image_url": "https://oriflamian-blog-store.s3.eu-central-1.amazonaws.com/63b4b271-accb-480d-9f97-984f2ceb3566.jpeg",
        "category_id": 2,
        "category": {
            "type": "wellness",
            "id": 2
        },
        "how_to_use": "replaces a meal",
        "description": "Shake Natural balance with strawberry flavor",
        "name": "wellness shake"
    },
    {
        "price": 9.99,
        "id": 5,
        "ingredients": "RICINUS COMMUNIS SEED OIL",
        "image_url": "https://oriflamian-blog-store.s3.eu-central-1.amazonaws.com/476a8bb1-3881-415f-98ea-9b46b3712ade.jpeg",
        "category_id": 3,
        "category": {
            "type": "make up",
            "id": 3
        },
        "how_to_use": "enjoy",
        "description": "put on the lips",
        "name": "Cream lipstick"
    },
    {
        "price": 29.99,
        "id": 8,
        "ingredients": "materials",
        "image_url": "https://oriflamian-blog-store.s3.eu-central-1.amazonaws.com/59e7b3ba-bf54-46d9-87d9-10708fea5600.jpeg",
        "category_id": 4,
        "category": {
            "type": "accessoires",
            "id": 4
        },
        "how_to_use": "enjoy",
        "description": "red",
        "name": "bag"
    },
    {
        "price": 29.99,
        "id": 9,
        "ingredients": "aroma",
        "image_url": "https://oriflamian-blog-store.s3.eu-central-1.amazonaws.com/bae7c569-0fd8-4211-a906-fc5bc05bb698.jpeg",
        "category_id": 5,
        "category": {
            "type": "fragrance",
            "id": 5
        },
        "how_to_use": "enjoy",
        "description": "style",
        "name": "eclat"
    }
]

## Create Post

### Request

`POST /post`

    curl -X POST http://127.0.0.1:5000/post \  
     -H "Authorization: Bearer <blogger token>"
     -H "Content-Type: application/json" \
     -d 
     {"title": "new post", "description": "this is new post", "photo": "/9j/decoded_photo==", "photo_extension": "jpeg"}
      
### Response

    HTTP/1.1 201 Created
    Date: Wed, 05 Jan 2022 10:54:52 GMT
    Status: 201 Created
    Connection: close
    Content-Type: application/json
    Content-Length: 197

  {
    "id": 2,
    "blogger_id": 1,
    "title": "new post",
    "photo_url": "https://oriflamian-blog-store.s3.eu-central-1.amazonaws.com/7bc72265-aa3b-45f2-9702-41675c79c4c7.jpeg",
    "date_created": "2022-08-23T14:29:44.398420",
    "description": "this is new post"
}

##

### Request

`POST /review`    

 curl -X POST http://127.0.0.1:5000/review \     
  -H "Authorization: Bearer <blogger token>"\
  -H "Content-Type: application/json" \
  
  -d {
  "title": "second Blogger review", 
  "comment": "This review is from Violeta for 1 post",
  "post_id": 1
  }
   
### Response

    HTTP/1.1 201 Created
    Date: Wed, 05 Jan 2022 12:50:34 GMT
    Status: 201 Created
    Connection: close
    Content-Type: application/json
    Content-Length: 53

    {
    "id": 6,
    "comment": "This review is from Violeta for 1 post",
    "title": "second Blogger review",
    "post_id": 1,
    "post_date": "2022-08-23T14:32:12.663407"
}
   
## Create Order

### Request

`POST /order`    

 curl -X POST http://127.0.0.1:5000/order \     
  -H "Authorization: Bearer <blogger token>"\
  -H "Content-Type: application/json" \
  
  -d {
  "products": [3, 3]
  }
   
### Response

    HTTP/1.1 201 Created
    Date: Wed, 05 Jan 2022 12:50:34 GMT
    Status: 201 Created
    Connection: close
    Content-Type: application/json
    Content-Length: 4

    {
    "id": 3,
    "products": [
        {
            "id": 4
        }
    ],
    "status": "Pending",
    "created_on": "2022-08-23T14:34:21.045099"
}

## Approve order
   
   
### Request
   
`PUT /admin/order/<int:id_>/approve`  

 curl -X PUT http://127.0.0.1:5000/admin/order/<int:id_>/approve \     
  -H "Authorization: Bearer <admin token>"\
  -H "Content-Type: application/json" \
  
 
   
### Response

    HTTP/1.1 200 OK
    Date: Wed, 05 Jan 2022 12:54:32 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 223

    204 NO CONTENT
    strip charging

## Reject Order

### Request
   
`PUT /admin/order/<int:id_>/reject`  

 curl -X PUT http://127.0.0.1:5000//admin/order/<int:id_>/reject \     
  -H "Authorization: Bearer <admin token>"\
  -H "Content-Type: application/json" \  
     
### Response

    HTTP/1.1 200 OK
    Date: Wed, 05 Jan 2022 12:54:32 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 21

    204 NO CONTENT

## Update Review

### Request
   
`PUT /blogger/reviw/<int:id>`  

 curl -X PUT http://127.0.0.1:5000/blogger/review/<int:id> \     
  -H "Authorization: Bearer <blogger token>"\
  -H "Content-Type: application/json" \
  -d {
  "title": "update review", 
  "comment": "this is Update review for 1 post", 
  "post_id": 1
  }
### Response

    HTTP/1.1 200 OK
    Date: Wed, 05 Jan 2022 12:54:32 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 21
  {
  "title": "update review", 
  "comment": "this is Update review for 1 post", 
  "post_id": 1
  }

  
## Delete Review
  

### Request
   
`DELETE /blogger/review/<int:id>`  

 curl -X DELETE http://127.0.0.1:5000/blogger/review/<int:id_> \     
  -H "Authorization: Bearer <blogger token>"\
  -H "Content-Type: application/json" \
  
     
### Response

    HTTP/1.1 204 NO CONTENT
    Date: Wed, 05 Jan 2022 12:54:32 GMT
    Status: 204 NO CONTENT
    Connection: close
    Content-Type: application/json
    

