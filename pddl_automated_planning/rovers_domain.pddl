(define (domain rover-exploration)
  (:requirements :strips :typing :fluents)
  (:types rover waypoint store camera mode lander objective)

  (:predicates
    (at ?r - rover ?w - waypoint)
    (at_lander ?l - lander ?w - waypoint)
    (can_traverse ?r - rover ?from - waypoint ?to - waypoint)
    (equipped_for_soil_analysis ?r - rover)
    (equipped_for_rock_analysis ?r - rover)
    (equipped_for_imaging ?r - rover)
    (empty ?s - store)
    (have_soil_analysis ?r - rover ?w - waypoint)
    (have_rock_analysis ?r - rover ?w - waypoint)
    (have_image ?r - rover ?o - objective ?m - mode)
    (communicated_soil_data ?w - waypoint)
    (communicated_rock_data ?w - waypoint)
    (communicated_image_data ?o - objective ?m - mode)
    (visible ?w1 - waypoint ?w2 - waypoint)
    (visible_from ?o - objective ?w - waypoint)
    (calibrated ?c - camera ?r - rover)
    (on_board ?c - camera ?r - rover)
  )

  (:action navigate
    :parameters (?r - rover ?from - waypoint ?to - waypoint)
    :precondition (and (at ?r ?from) (can_traverse ?r ?from ?to) (visible ?from ?to))
    :effect (and (not (at ?r ?from)) (at ?r ?to))
  )

  (:action sample_soil
    :parameters (?r - rover ?s - store ?w - waypoint)
    :precondition (and (at ?r ?w) (equipped_for_soil_analysis ?r) (empty ?s))
    :effect (and (not (empty ?s)) (have_soil_analysis ?r ?w))
  )

  (:action communicate_soil_data
    :parameters (?r - rover ?l - lander ?w - waypoint ?r_pos - waypoint ?l_pos - waypoint)
    :precondition (and (at ?r ?r_pos) (at_lander ?l ?l_pos) (have_soil_analysis ?r ?w) (visible ?r_pos ?l_pos))
    :effect (and (communicated_soil_data ?w))
  )
)
