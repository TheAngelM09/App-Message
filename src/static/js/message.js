document.addEventListener('DOMContentLoaded', function(){
    const phone = "584121234567"
    const company = "1"
    getConversation(company, phone)
});

function getTime(timestamp){
    const date = new Date(timestamp);
    const time = `${date.getHours()}:${date.getMinutes()}`
    return time
};

function getConversation(company, phone){
    $.ajax({
        url: `/conv/get?company=${company}&phone=${phone}`,
        type: "GET",
        success: function(response){
            let message = "";
            response[0].forEach(msg => {
                if(msg["type"] == "company"){
                    message += `<div class="row message-body">
                        <div class="col-sm-12 message-main-receiver">
                            <div class="receiver">
                            <div class="message-text">
                        ${msg["message"]}
                            </div>
                            <span class="message-time pull-right">
                                ${getTime(msg["timestamp"])}
                            </span>
                            </div>
                        </div>
                    </div>`
                }else{
                    message += `<div class="row message-body">
                        <div class="col-sm-12 message-main-sender">
                            <div class="sender">
                            <div class="message-text">
                        ${msg["message"]}
                            </div>
                            <span class="message-time pull-right">
                                ${getTime(msg["timestamp"])}
                            </span>
                            </div>
                        </div>
                    </div>`
                }
            });
            $("#body_message").html(message)           
        },
        error: function(xhr){
            console.error("Error: ", xhr.responseText);
        }
    });
}

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
                                display_phone_number: "584121234567",
                                phone_number_id: "133711623159384"
                            },
                            contacts: [
                                {
                                    profile: {
                                        name: "John Doe"
                                    },
                                    wa_id: "584121234567"
                                }
                            ],
                            messages: [
                                {
                                    from: "584121234567",
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
        contentType: "application/json",
        success: function(response){
            console.log(response);
        },
        error: function(xhr){
            console.error("Error: ", xhr.responseText);
        }
    });
});