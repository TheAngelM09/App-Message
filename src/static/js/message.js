$("#send").click(function(){
    let message = {
        object: "whatsapp_business_account",
        entry: [
            {
                id: "130958976769754",
                changes: [
                    {
                        value: {
                            messaging_product: "whatsapp",
                            metadata: {
                                display_phone_number: "584241234567",
                                phone_number_id: "133711623159384"
                            },
                            contacts: [
                                {
                                    profile: {
                                        name: "John Doe"
                                    },
                                    wa_id: "584241234567"
                                }
                            ],
                            messages: [
                                {
                                    from: "51938592888",
                                    id: "wamid.HBgLNTE5NzAyNDQwMjYVAgASGCAyOUE5OTI1RjZDRUMyODZCQzQxRTg0N0RFQTRGREFBQwA=",
                                    timestamp: Date.now(),
                                    text: {
                                        body: $("#message").val(),
                                    },
                                    type: "text"
                                }
                            ]
                        },
                        field: "messages"
                    }
                ]
            }
        ]
    };

    $.ajax({
        url: "/msg/ws",
        type: "POST",
        data: JSON.stringify(message),
        contentType: "application/JSON",
        success: function(response){
            console.log(response);
        },
        error: function(xhr){
            console.error("Error: ", xhr.responseText);
        }
    });
});