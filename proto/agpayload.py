syntax = "proto2"

enum action {

register_farmer:0;
register_buyer:1;
register_transporter:2;
otp_transaction:3;
}


message register_farmer{
  required string public_key = 1;
  required string aadhar_card = 2;
  required uint64 timestamp = 3;    //will not be updated
  required string full_name = 4;
  required state State = 5;
  required uint32 pincode = 6;
  required uint32 mobilenumber = 7;
  required string district= 8;
  optional bytes photo = 9;      //change to required in production build
  optional string transaction_id = 10;
}

message register_buyer{
  required string public_key = 1;
  required string aadhar_card = 2;
  required uint64 timestamp = 3;    //will not be updated
  required string full_name = 4;
  required state State = 5;
  required uint32 pincode = 6;
  required uint32 mobilenumber = 7;
  required string district = 8;
  optional string transaction_id =9;
}

message register_transporter{
  required string public_key = 1;
  required string aadhar_card = 2;
  required uint64 timestamp = 3;    //will not be updated
  required string full_name = 4;
  required state State = 5;
  required uint32 pincode = 6;
  required uint32 mobilenumber = 7;
  required string district = 8;
  required string driving_license = 9;
  optional bytes photo = 10;       //change to required in production build
  optional string transaction_id = 11;
}

message otp_transaction{
    required string mobilenumber = 1;
    required uint32 otp =2;
    required public_key =3 ;

}

message Realpayload{
    #ACTION WILL STATE WHAT TO EXPECT IN PAYLOAD
    required action Action = 1;
    # ANYONE OF THE FOLLOWING ACTIONS WILL BE SELECTED
    register_farmer reg_far = 2;
    register_buyer reg_buy = 3;
    register_transporter reg_tra = 4;
    otp_transaction otp_tra = 5;
}
