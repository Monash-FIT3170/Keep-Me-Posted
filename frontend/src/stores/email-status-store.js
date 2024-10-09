// gets written to "sent" when the email is sent, used to reflect sent status on UI
import { writable } from 'svelte/store'

export const emailStatusStore = writable("")
