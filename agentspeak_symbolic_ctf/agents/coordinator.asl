// Coordinator Agent (BDI AgentSpeak)
// Manages global situational awareness and dynamic role assignment

+!init_coordinator
    <- .print("Coordinator Agent initialized. Broadcasting ready state.");
       +base_position(0, 0);
       +enemy_base_position(100, 100);
       !patrol_schedule.

+enemy_spotted(X, Y, Type)[source(Ag)]
    : not target_threat(X, Y)
    <- +target_threat(X, Y);
       .print("Hostile detected at (", X, ",", Y, ") by agent ", Ag);
       .broadcast(tell, alert_threat(X, Y));
       !dispatch_interceptor(X, Y).

+flag_dropped(X, Y)[source(Ag)]
    <- .print("Critical Alert: Flag dropped at (", X, ",", Y, ")");
       .broadcast(achieve, secure_flag(X, Y)).

+!dispatch_interceptor(X, Y)
    : free_attacker(Attacker)
    <- .send(Attacker, achieve, intercept(X, Y));
       -free_attacker(Attacker).
