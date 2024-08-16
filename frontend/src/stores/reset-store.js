import { apiStatusStore } from "./api-status-store";
import { ContactsStore } from "./contacts-store";
import { emailStatusStore } from "./email-status-store";
import { summaryStore} from "./summary-store";
import { transcriptStore, sendWithTranscriptStore } from "./transcript-store";
import { isOpen, isCancelled } from "./user-email-popup-store";

export function resetStores() { 
    
    apiStatusStore.set("");
    ContactsStore.set([]);
    emailStatusStore.set("")
    summaryStore.set({
        summary: "",
        subject: ""
    })
    transcriptStore.set({
        transcript: ""
    })
    sendWithTranscriptStore.set(false)
    isOpen.set(false)
    isCancelled.set(false)

}