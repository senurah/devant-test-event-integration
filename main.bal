import ballerina/log;
import ballerinax/rabbitmq;

listener rabbitmq:Listener eventListener = new (host = host, port = port, username = username, password = password);

service rabbitmq:Service "Orders" on eventListener {
    remote function onMessage(rabbitmq:AnydataMessage message, rabbitmq:Caller caller) returns error? {
        do {
            log:printInfo(message.toString());
        } on fail error err {
            // handle error
            return error("unhandled error", err);
        }
    }

    remote function onError(rabbitmq:AnydataMessage message, rabbitmq:Error rabbitmqError) returns error? {
        do {
        } on fail error err {
            // handle error
            return error("unhandled error", err);
        }
    }
}
