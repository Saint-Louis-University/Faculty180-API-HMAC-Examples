library(httr)

# configuration
public_key <- "Y5aNy8OZRYFKlTxNzXuSxzz64M8YLQB3vrcUP1zk7wQ="
private_key <- "uEvu95GRt8fYw8dZkOyQGsOLy5yuB9vcUEK5cAcNuB4X6D6pTJegoIp/yRa7GaP/Lf6CQIA/xI/oP//YkayuAByx0nieazUEqp3DR7FtNf43="
database_id <- "TestUniv"

# HTTP request details
request_verb <- "GET"
host <- "https://faculty180.interfolio.com/api.php"
request_string <- "/units"
timestamp_string <- format(as.POSIXlt(Sys.time(), "UTC"), "%Y-%m-%d %H:%M:%S")

# format for HMAC
verb_request_string <- paste(request_verb, "\n",  timestamp_string, request_string, sep = "\n")
signed_hash <- hmac_sha1(private_key, verb_request_string)
authorization_header <- paste0("INTF ", public_key, ":", signed_hash)

# issue request
url <- paste0(host, request_string)
config <- httr::add_headers("TimeStamp" = timestamp_string, 
                            "Authorization" = authorization_header, 
                            "INTF-DatabaseID" = database_id)
response <- httr::GET(url, config)
paste("TimeStamp:", timestamp_string)
paste("Authorization:", authorization_header)
paste("INTF-DatabaseID:", database_id)
content(response, "text", encoding = "UTF-8")
