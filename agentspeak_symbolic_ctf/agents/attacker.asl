// Attacker Agent (BDI AgentSpeak)
// Offensive flag extraction and escort logic

+!init_attacker
    <- .print("Attacker Agent initialized.");
       +state(infiltrating);
       !infiltrate_base.

+!infiltrate_base
    : enemy_base_position(TX, TY) & state(infiltrating)
    <- .print("Infiltrating enemy perimeter at (", TX, ",", TY, ")");
       moveTo(TX, TY).

+at_flag_position(X, Y)
    <- grabFlag;
       -+state(extracting);
       .broadcast(tell, flag_acquired(X, Y));
       !return_to_base.

+!return_to_base
    : base_position(BX, BY)
    <- .print("Extracting flag to home base at (", BX, ",", BY, ")");
       moveTo(BX, BY).

+under_fire(AttackerID)
    : state(extracting)
    <- .broadcast(tell, need_reinforcements(AttackerID));
       evasive_maneuver.
