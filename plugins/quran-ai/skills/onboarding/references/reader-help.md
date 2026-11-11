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
- **Selection:** with Content on Auto and nothing selected, briefly tap a word
  in the active ayah to focus that word and show its word meanings; tap the
  focused word again to return to the whole ayah and its translation. A tap on
  a word in another ayah moves there and keeps what the panel was showing.
  An ayah number moves the cursor to the start of that ayah. While the
  recitation plays, a tap on any word moves the recitation to that word and
  keeps what the panel was showing; a tap outside a selection still clears it. Hold a word still to step through three stages, all
  timed from the moment the finger goes down: the whole ayah (618 ms by
  default), the word alone (1000 ms), then cancel (1618 ms), which leaves
  everything as it was; the stages repeat while the hold continues. The shown
  stage commits on release. The base time and the multiplier between stages are
  adjustable in Experiments. A tap on a word inside a selection keeps the
  selection and moves the cursor there, which is where listening starts (inside
  a selection of whole ayahs, to the start of the tapped ayah while silent); a tap
  on a word outside clears the selection and focuses that word. A tap never
  grows or shrinks a selection: hold and drag to resize it, starting inside
  it, or starting outside and releasing inside it. A hold and drag entirely
  outside adds a separate selection. Tapping a selection of exactly one word
  clears it. On touch a vertical movement scrolls, while a deliberate sideways
  movement out of the word along its line selects. Shift extends a range;
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
- **Contextual meaning:** in Auto, a selection of whole ayahs shows
  translations and any selection that cuts through an ayah shows word meanings.
  Without a selection, focusing a word shows word meanings and tapping the
  focused word shows the whole-ayah translation again. Moving to another ayah,
  by Prev, Next or the arrow keys, keeps whichever of the two was showing.
  These actions do not change the saved Content preference. Settings → Translation → Content can keep
  it on Whole ayah or Word by word instead, and also provides Translator, Panel
  position (Top or Bottom), and Start minimized. Word by word, the left arrow
  moves to the previous word and the right arrow to the next; hold to keep
  moving. Arrows do not create a selection; a selected word moves with the
  arrow, so the selection becomes the one word the cursor lands on. Tap a word if the panel has no context. Click the panel's tab
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
- **Keyboard:** while the reader has focus and the whole ayah is showing,
  all four arrows move between ayahs. While a word is focused or selected,
  Left/Right move one word in reading order, across ayahs, and Up/Down move to
  the word at the same position on the line above or below; pressing the
  opposite arrow next returns to the word just left. A selection of one whole
  ayah or one word moves with the arrow. Shift with arrows extends or shortens
  a range. Escape clears selected words, then the focused word, then the
  active ayah. Tab does not leave the Mushaf. Enter confirms a surah or page
  change; Escape closes that control. Keyboard navigation then returns to the
  Mushaf.
- **Continue studying:** keep the reader beside the conversation where the
  host supports it. Links in answers return to the passages being discussed.
  Opening a link activates its passage for Copy, Lastmarks, and current
  reader context, and Back returns to where you were. Ask about that active passage, or
  select a more specific phrase. To keep passages for a later question, save
  them in the Ledger. Follow useful links in the next answer to keep reading
  and discovering. If the user asks to resume, follow the Interactive Study
  skill's current resume instructions.
