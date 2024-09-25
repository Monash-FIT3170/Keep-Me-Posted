import { writable } from 'svelte/store'

export const ResetPasswordStore = writable({
    email: "",
    code: ""
})