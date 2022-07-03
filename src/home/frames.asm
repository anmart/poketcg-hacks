; calls DoFrame a times
DoAFrames:
.loop
	push af
	call DoFrame
	pop af
	dec a
	jr nz, .loop
	ret

; updates background, sprites and other game variables, halts until vblank, and reads user input
; if wDebugPauseAllowed is not 0, the game can be paused (and resumed) by pressing the SELECT button
DoFrame:
	push af
	push hl
	push de
	push bc
	ld hl, wDoFrameFunction ; context-specific function
	call CallIndirect
	call WaitForVBlank
	call ReadJoypad
	call HandleDPadRepeat
	;ld a, [wDebugPauseAllowed]
	;or a
	;jr z, .done
	ldh a, [hKeysHeld]
	and SELECT
	jr z, .done
	ldh a, [hKeysHeld]
	and D_PAD | B_BUTTON
	jr z, .done
.game_paused_loop
	call WaitForVBlank
	call ReadJoypad
	call HandleDPadRepeat
	ldh a, [hKeysPressed]
	and B_BUTTON | SELECT
	jr z, .game_paused_loop
	; probably hacky, but should prevent menu presses from affecting game too much
	ld a, [hKeysPressed]
	ld [hKeysHeld], a
	xor a
	ld [hKeysPressed], a
.done
	pop bc
	pop de
	pop hl
	pop af
	ret

; handle D-pad repeat counter
; used to quickly scroll through menus when a relevant D-pad key is held
HandleDPadRepeat:
	ldh a, [hKeysHeld]
	ldh [hDPadHeld], a
	and D_PAD
	jr z, .done
	ld hl, hDPadRepeat
	ldh a, [hKeysPressed]
	and D_PAD
	jr z, .dpad_key_held
	ld [hl], 24
	ret
.dpad_key_held
	dec [hl]
	jr nz, .done
	ld [hl], 6
	ret
.done
	ldh a, [hKeysPressed]
	and BUTTONS
	ldh [hDPadHeld], a
	ret
