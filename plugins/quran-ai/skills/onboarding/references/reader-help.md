# Reader controls and settings

For later help, answer the specific question directly using only the relevant
guidance below. Do not restart onboarding or reopen the reader for a settings
or usage question.

- **Settings:** prefer **Reader settings** on quran.ai's native **Manage** page
  when available. It mirrors the reader’s **Reader**, **Translation**, and **More**
  tabs as closely as the host form allows. Reader contains Theme, Text size,
  and Navigation. Translation contains Content (Auto: match context, the
  default; Whole ayah; or Word by word) with its Translator, then Panel position
  and Start minimized. More contains Copy text. Navigation's Button placement shows where Prev
  and Next sit; drag either button to a reader edge or the footer. Buttons on
  the same side move by ayah; buttons on opposite sides move by screen. Ayah
  placement offers Keep in view (the default) or Beside translation / Beside
  word meanings. Keep in view moves an ayah only when needed to make it visible.
  The other option aligns it beside the translation or word meanings when an
  ayah navigation control is pressed or a word arrow crosses into another ayah.
  Moving by screen instead offers Select first visible ayah.
  The reader's Settings control remains available where shown. If the user asks
  to open settings and `interactive_study_settings_open`
  is available, use it; do not invent settings tools or claim a preference was
  saved without confirmation from the settings surface.
- **Selection:** briefly tap a different word to move the cursor and active color
  there without a bounded selection. Briefly tap the currently active colored
  word to keep that precise position, release any selection and show its whole
  ayah. Its own ayah number or margin does the same; another ayah's number or
  margin moves to that ayah's first word. Hold a word to the first threshold
  (400 ms by default), then release for a bounded whole-ayah selection. Keep
  holding to the later word threshold (800 ms by default), then release for a
  bounded word. The two thresholds are independently adjustable in Experiments.
  The shown stage commits on release, not while the finger is still down.
  Drag across words for a phrase; on touch a vertical movement scrolls, while
  a deliberate sideways movement out of the word along its line selects.
  Drag a selected span's first or last word to resize it. A short tap beside a
  span focuses that word and clears the span; it does not extend it. Holds can
  add ayahs or words to existing selections. A hold on an already selected
  ayah previews removing that ayah; release commits it. Shift extends a range;
  Ctrl/Cmd adds or removes selected words, phrases or whole ayahs.
- **Ask with passages:** **Study tools** starts open in **Quick send**: type a
  question and send it with the current selection. Choose **Ledger** to keep
  selections with notes (**Add to ledger**). Tick notes and choose **Send to
  ChatGPT** (or **Send to Claude**) to add them to the prompt box, then write
  and send your question there. The current selection also reaches the AI as
  background context with your next message. Reloading or closing a reader may
  clear notes added to the prompt box but not yet sent, depending on the host.
  Use the gutter button to reopen Study tools after closing it. In the expanded
  ledger, the book button beside each item's checkbox reopens the reader at that
  saved selection.
- **Navigation:** tap the surah name or page number to change location.
  The upper and lower corner controls move backward and forward; hold to
  keep moving. Reader → Navigation → Button placement shows whether they move
  by ayah or by screen.
- **Contextual meaning:** in Auto, a bounded word selection shows word meanings
  and whole-ayah selections show translations. Without a selection, tapping a
  different word shows word meanings; tapping the active colored word, its ayah
  number or its margin shows the whole-ayah translation while keeping the precise
  cursor. These actions do not change the saved Content preference. Settings → Translation → Content can keep
  it on Whole ayah or Word by word instead, and also provides Translator, Panel
  position (Top or Bottom), and Start minimized. Word by word, the left arrow
  moves to the previous word and the right arrow to the next; hold to keep
  moving. Arrows do not create a selection; an existing range stays selected
  while the cursor remains inside it. Tap a word if the panel has no context. Click the panel's tab
  to collapse or expand it; drag the tab to resize the panel, and drag beyond
  its expansion limit to preview the opposite dock. Release while that preview
  is showing to switch docks.
- **Copying:** Settings → More → Copy text previews selected text (or, with
  nothing selected, the first ayah on the page) and controls Diacritics (With
  diacritics or Letters only), Ayah marker (Surah & ayah, Ayah only, or None),
  and Between ayat (Same line or New line). Copy text copies the preview;
  Copy deeplink copies a link to the selection. If the host blocks clipboard
  buttons, use the device’s copy command on the selected preview text.
- **Feedback:** choose **Send feedback** in the reader menu, below **Reader
  settings**, to send an idea or report a bug. The AI host reviews and submits the feedback.
- **Clear selection:** while something is selected, a small dash tab beside the
  Prev and Next buttons clears it in one tap.
- **Back and Forward:** after a jump of more than a page (a surah or page
  change, a Lastmark, a ledger note, or a link), Back leads the selection and
  display pill and names its destination, such as Back to al-Baqarah 255. It
  restores that screen with the selection you had. Selecting a new ayah two or
  more pages from the previous selection counts too; reading on, turning pages,
  and extending a selection do not. If the selection is more than a screen away,
  Back first brings it back into view. Forward appears after going back. The
  one you used last leads while it has places left, so pressing it again keeps
  going the same way; jumping somewhere new puts Back first again. Each reader
  keeps its last ten places.
- **Keyboard:** while the reader has focus, Up/Down move between ayahs and
  Left/Right move the word cursor in reading order. Shift with arrows extends
  or shortens a range. Escape clears selected words, then the active word,
  then the active ayah. Enter confirms a surah or page change; Escape closes
  that control. Keyboard navigation then returns to the Mushaf.
- **Continue studying:** keep the reader beside the conversation where the
  host supports it. Links in answers return to the passages being discussed.
  Opening a link activates its passage for Copy, Lastmarks, and current
  reader context, and Back returns to where you were. Ask about that active passage, or
  select a more specific phrase. To keep passages for a later question, save
  them in the Ledger. Follow useful links in the next answer to keep reading
  and discovering. If the user asks to resume, follow the Interactive Study
  skill's current resume instructions.
