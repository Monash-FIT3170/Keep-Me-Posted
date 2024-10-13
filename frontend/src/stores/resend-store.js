import { writable } from "svelte/store";

export const summaryStore = writable({
  subject: "",
  transcript: "",
});
