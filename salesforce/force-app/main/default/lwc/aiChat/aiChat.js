import { LightningElement } from 'lwc';
import getAIResponse from '@salesforce/apex/AiChatController.getAIResponse';

export default class AiChat extends LightningElement {


    userQuestion = '';  //store user type
    submittedQuestion = '';  //store user question
    aiResponse = ''; //store ai response


    handleInputChange(event){
        this.userQuestion = event.target.value;
    }

    async handleSend(){
        this.submittedQuestion = this.userQuestion;

        try{

            const result = await getAIResponse({question : this.submittedQuestion})
            this.aiResponse = result;

        } catch(error){
            console.error(error);
        }

    }


}