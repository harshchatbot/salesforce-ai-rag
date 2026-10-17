public with sharing class AiChatController {

   
    @AuraEnabled
    public static String getAIResponse(String question){

        HttpRequest req = new HttpRequest();

        req.setEndpoint('callout:Salesforce_RAG_API/ask');
        req.setMethod('POST');
        req.setHeader('Content-Type', 'application/json');

        Map<String,String> jsonBody = new Map<String,String>(); // as fatapi backend expects "question": "What is RAG?"
        jsonBody.put('question', question);
        String requestBody = JSON.serialize(jsonBody);
        req.setBody(requestBody);

        Http http = new Http();
        HttpResponse response = http.send(req);

        if(response.getStatusCode() == 200){

            Map<String,Object> resBody = (Map<String,Object>) JSON.deserializeUntyped(response.getBody());
            String answer = (String) resBody.get('answer');

            return answer;

        }

        return 'AI service unavailable';

    }
}