INCLUDE "macros/opening_sequence.asm"

OpeningSequence: ; 1d59d (7:559d)
	opening_seq_load_charizard_scene
	opening_seq_play_sfx SFX_58
	opening_seq_set_orbs_coordinates OpeningOrbCoordinates_CharizardScene
	opening_seq_set_orbs_animations OpeningOrbAnimations_CharizardScene
	opening_seq_wait 44
	opening_seq_fade_in
	opening_seq_wait 44
	opening_seq_fade_out
	opening_seq_wait 30

	opening_seq_load_scyther_scene
	opening_seq_play_sfx SFX_58
	opening_seq_set_orbs_coordinates OpeningOrbCoordinates_ScytherScene
	opening_seq_set_orbs_animations OpeningOrbAnimations_ScytherScene
	opening_seq_wait 44
	opening_seq_fade_in
	opening_seq_wait 44
	opening_seq_fade_out
	opening_seq_wait 30
	
	opening_seq_load_aerodactyl_scene
	opening_seq_play_sfx SFX_59
	opening_seq_set_orbs_coordinates OpeningOrbCoordinates_AerodactylScene
	opening_seq_set_orbs_animations OpeningOrbAnimations_AerodactylScene
	opening_seq_wait 44
	opening_seq_fade_in
	opening_seq_wait 100
	opening_seq_fade_out
	opening_seq_wait 60

	opening_seq_load_title_screen_scene
	opening_seq_play_sfx SFX_5A
	opening_seq_set_orbs_coordinates OpeningOrbCoordinates_InitialTitleScreen
	opening_seq_set_orbs_animations OpeningOrbAnimations_InitialTitleScreen
	opening_seq_wait_orbs_animation
	opening_seq_fade_in
	opening_seq_wait 16
	opening_seq_play_sfx SFX_5B
	opening_seq_set_orbs_coordinates OpeningOrbCoordinates_InTitleScreen
	opening_seq_set_orbs_animations OpeningOrbAnimations_InTitleScreen
	opening_seq_wait_sfx
	opening_seq_play_title_screen_music
	opening_seq_wait 60
	opening_seq_end
; 0x1d614
