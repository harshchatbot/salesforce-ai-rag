public with sharing class AiChatController {
   
    @AuraEnabled
    public static String getAIResponse(String question){

        return 'AI received your question: ' + question;

    }
}