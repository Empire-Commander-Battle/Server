import string

dword      = 0x8000000000000000
dword_mask = 0xffffffffffffffff

density_bits      = 32
fkf_density_mask  = 0xFFFF #16K

#terain condition flags
fkf_plain             = 0x00000004
fkf_steppe            = 0x00000008
fkf_snow              = 0x00000010
fkf_desert            = 0x00000020
fkf_plain_forest      = 0x00000400
fkf_steppe_forest     = 0x00000800
fkf_snow_forest       = 0x00001000
fkf_desert_forest     = 0x00002000
fkf_terrain_mask      = 0x0000ffff

fkf_realtime_ligting  = 0x00010000 #deprecated
fkf_point_up          = 0x00020000 #uses auto-generated point-up(quad) geometry for the flora kind
fkf_align_with_ground = 0x00040000 #align the flora object with the ground normal
fkf_grass             = 0x00080000 #is grass
fkf_on_green_ground   = 0x00100000 #populate this flora on green ground
fkf_rock              = 0x00200000 #is rock
fkf_tree              = 0x00400000 #is tree -> note that if you set this parameter, you should pass additional alternative tree definitions
fkf_snowy             = 0x00800000
fkf_guarantee         = 0x01000000

fkf_speedtree         = 0x02000000  #NOT FUNCTIONAL: we have removed speedtree support on M&B Warband

fkf_has_colony_props  = 0x04000000  # if fkf_has_colony_props -> then you can define colony_radius and colony_treshold of the flora kind


def density(g):
  if (g > fkf_density_mask):
    g = fkf_density_mask
  return ((dword | g) << density_bits)


fauna_kinds = [


  ("grass",fkf_grass|fkf_on_green_ground|fkf_guarantee|fkf_align_with_ground|fkf_point_up|fkf_plain|fkf_plain_forest|density(1500),[["grass_amm","0"],["grass_bmm","0"],["grass_cmm","0"],["grass_dmm","0"],["grass_emm","0"],["grass_fmm","0"],["grass_gmm","0"],["grass_hmm","0"],["grass_imm","0"],["grass_jmm","0"],["grass_kmm","0"]]),
  ("fern",fkf_plain_forest|fkf_align_with_ground|density(100),[["fern_bmm","0"],["fern_amm","0"],["fern_b2mm","0"],["fern_b4mm","0"],["fern_b3mm","0"],["fern_b5mm","0"]]),
  ("grass_steppe",fkf_grass|fkf_on_green_ground|fkf_guarantee|fkf_align_with_ground|fkf_point_up|fkf_steppe|fkf_steppe_forest|density(1500),[["grass_yellow_amm","0"],["grass_yellow_bmm","0"],["grass_yellow_cmm","0"],["grass_yellow_dmm","0"],["grass_yellow_emm","0"]]),


  ("thorn_a",fkf_align_with_ground|fkf_plain|fkf_plain_forest|density(150),[["thorn_a","0"],["thorn_b","0"],["thorn_c","0"],["thorn_d","0"]]),
  ("basak",fkf_plain|fkf_plain_forest|fkf_steppe|fkf_steppe_forest|density(50),[["basak","0"]]),
  ("small_plant",fkf_plain|fkf_plain_forest|fkf_steppe|fkf_steppe_forest|fkf_align_with_ground|density(50),[["small_plant","0"],["small_plant_b","0"],["small_plant_c","0"]]),
  ("buddy_plant",fkf_plain|fkf_plain_forest|fkf_steppe|fkf_steppe_forest|fkf_align_with_ground|density(50),[["buddy_plant","0"],["buddy_plant_b","0"]]),
  ("yellow_flower",fkf_plain|fkf_plain_forest|fkf_steppe|fkf_steppe_forest|fkf_align_with_ground|density(50),[["grass_bush_imm","0"],["grass_bush_cmm","0"]]),
  ("spiky_plant",fkf_plain|fkf_plain_forest|fkf_steppe|fkf_steppe_forest|fkf_align_with_ground|density(50),[["spiky_plantmm","0"],["spiky_plantmm2","0"],["spiky_plantmm3","0"],["spiky_plantmm4","0"],["spiky_plantmm5","0"],["spiky_plantmm6","0"]]),
  ("seedy_plant",fkf_plain|fkf_plain_forest|fkf_steppe|fkf_steppe_forest|fkf_align_with_ground|density(50),[["seedy_plant_a","0"]]),
  ("blue_flower",fkf_plain|fkf_plain_forest|fkf_steppe|fkf_steppe_forest|fkf_align_with_ground|density(30),[["grass_bush_c3mm","0"]]),
  ("big_bush",fkf_plain|fkf_plain_forest|fkf_align_with_ground|density(20),[["big_bushmm","0"],["big_bushmm2","0"],["big_bushmm3","0"],["big_bushmm4","0"],["big_bushmm5","0"],["big_bushmm6","0"],["big_bushmm7","0"]]),

  ("mm_small_rock",fkf_plain|fkf_align_with_ground|fkf_plain_forest|fkf_steppe|fkf_steppe_forest|fkf_realtime_ligting|fkf_rock|density(5),[["stone1","bo_stone1"],["stone2","bo_stone2"],["stone3","bo_stone3"],["stone4","bo_stone4"],["stone5","bo_stone5"],["stone6","bo_stone6"]]),
  ("small_rock",fkf_plain|fkf_align_with_ground|fkf_plain_forest|fkf_steppe|fkf_steppe_forest|fkf_realtime_ligting|fkf_rock|density(5),[["rock_c","bo_rock_c"],["rock_d","bo_rock_d"],["rock_e","bo_rock_e"],["rock_f","bo_rock_f"],["rock_g","bo_rock_g"],["rock_h","bo_rock_h"],["rock_i","bo_rock_i"],["rock_k","bo_rock_k"]]),
  ("mm_big_rock",fkf_plain|fkf_align_with_ground|fkf_plain_forest|fkf_steppe|fkf_steppe_forest|fkf_realtime_ligting|fkf_rock|density(1),[["rock_001","bo_rock_001"],["rock_002","bo_rock_002"],["rock_003","bo_rock_003"],["rock_004","bo_rock_004"],["rock_005","bo_rock_005"],["rock_007","bo_rock_007"],["rock_009","bo_rock_009"],["rock_010","bo_rock_010"],["rock_011","bo_rock_011"],["rock_012","bo_rock_012"],["rock_013","bo_rock_013"],["rock_014","bo_rock_014"],["rock_008","bo_rock_008"]]),
  ("rock_snowy",fkf_snow|fkf_align_with_ground|fkf_snow_forest|fkf_realtime_ligting|fkf_rock|density(5),[["rock_snowy_a","bo_rock_snowy_a"],["rock_snowy_b","bo_rock_snowy_b"],["rock_snowy_c","bo_rock_snowy_c"],]),
  ("rock",fkf_plain|fkf_align_with_ground|fkf_plain_forest|fkf_steppe|fkf_steppe_forest|fkf_realtime_ligting|fkf_rock|density(50),[["rock1","bo_rock1"],["rock2","bo_rock2"],["rock3","bo_rock3"],["rock4","bo_rock4"],["rock5","bo_rock5"],["rock7","bo_rock7"]]), # patch1115 bug fix 42/4
  ("rock_snowy2",fkf_snow|fkf_align_with_ground|fkf_snow_forest|fkf_realtime_ligting|fkf_rock|density(5),[["rock1_snowy","bo_rock1"],["rock2_snowy","bo_rock2"],["rock6_snowy","bo_rock6"],]),

  ("bush_new_1",density(0),[["bush_a01","0"],["bush_a02","0"]]),
  ("bush_new_2",density(0),[["bush_new_amm","0"],["bush_new_bmm","0"],["bush_new_cmm","0"],["bush_new_dmm","0"],["bush_new_emm","0"],["bush_new_fmm","0"]]),
  ("bush_new_3",density(0),[["bush_new_b","0"]]),
  ("bush_new_4",density(0),[["bush_new_c","0"]]),

  ("grape_vineyard",density(0),[("grape_vineyard","bo_grape_vineyard")]),
  ("grape_vineyard_stake",density(0),[("grape_vineyard_stake","bo_grape_vineyard_stake")]),

  ("wheat",fkf_plain|fkf_plain_forest|fkf_steppe|fkf_steppe_forest|density(40),[["wheat_a","0"],["wheat_b","0"],["wheat_c","0"],["wheat_d","0"]]),

  ("valleyRock_rounded",fkf_rock|fkf_realtime_ligting|density(5),[["valleyRock_rounded_1","bo_valleyRock_rounded_1"],["valleyRock_rounded_2","bo_valleyRock_rounded_2"],["valleyRock_rounded_3","bo_valleyRock_rounded_3"],["valleyRock_rounded_4","bo_valleyRock_rounded_4"]]),
  ("valleyRock_flat",fkf_rock|fkf_realtime_ligting|density(5),[["valleyRock_flat_1","bo_valleyRock_flat_1"],["valleyRock_flat_2","bo_valleyRock_flat_2"],["valleyRock_flat_3","bo_valleyRock_flat_3"],["valleyRock_flat_4","bo_valleyRock_flat_4"],["valleyRock_flat_5","bo_valleyRock_flat_5"],["valleyRock_flat_6","bo_valleyRock_flat_6"]]),
  ("valleyRock_flatRounded_small",fkf_rock|fkf_realtime_ligting|density(5),[["valleyRock_flatRounded_small_1","bo_valleyRock_flatRounded_small_1"],["valleyRock_flatRounded_small_2","bo_valleyRock_flatRounded_small_2"],["valleyRock_flatRounded_small_3","bo_valleyRock_flatRounded_small_3"]]),
  ("valleyRock_flatRounded_big",fkf_rock|fkf_realtime_ligting|density(5),[["valleyRock_flatRounded_big_1","bo_valleyRock_flatRounded_big_1"],["valleyRock_flatRounded_big_2","bo_valleyRock_flatRounded_big_2"]]),

  # patch1115 bug fix 42/2 start
  ("mm_aspen",fkf_tree|density(0),[["mm_aspen1","bo_mm_aspen1",("0","0")],["mm_aspen2","bo_mm_aspen2",("0","0")],["mm_aspen3","bo_mm_aspen3",("0","0")],["mm_aspen4","bo_mm_aspen4",("0","0")],["mm_aspen5","bo_mm_aspen5",("0","0")],["mm_aspen6","bo_mm_aspen6",("0","0")],["mm_aspen7","bo_mm_aspen7",("0","0")],["mm_aspen8","bo_mm_aspen8",("0","0")],["mm_aspen9","bo_mm_aspen9",("0","0")],["mm_aspen10","bo_mm_aspen10",("0","0")],["mm_aspen11","bo_mm_aspen11",("0","0")],["mm_aspen12","bo_mm_aspen12",("0","0")],["mm_aspen13","bo_mm_aspen13",("0","0")],["mm_aspen14","bo_mm_aspen14",("0","0")],["mm_aspen15","bo_mm_aspen15",("0","0")]]),
  ("mm_pine_snowy",fkf_snow|fkf_snow_forest|fkf_tree|density(4),[["mm_pine1s","bo_mm_pine1s",("0","0")],["mm_pine2s","bo_mm_pine2s",("0","0")],["mm_pine3s","bo_mm_pine3s",("0","0")],["mm_pine4s","bo_mm_pine4s",("0","0")],["mm_pine5s","bo_mm_pine5s",("0","0")],["mm_pine6s","bo_mm_pine6s",("0","0")],["mm_pine7s","bo_mm_pine7s",("0","0")]]),
  ("mm_northern",fkf_plain|fkf_plain_forest|fkf_tree|fkf_steppe|fkf_steppe_forest|density(4),[["mm_pine_3","bo_mm_pine_3",("0","0")],["mm_pine_4","bo_mm_pine_4",("0","0")],["mm_pine_5","bo_mm_pine_5",("0","0")],["mm_northern_tree1","bo_mm_northern_tree1",("0","0")],["mm_northern_tree2","bo_mm_northern_tree2",("0","0")]]),
  ("mm_autumn_tree",fkf_steppe|fkf_steppe_forest|fkf_tree|density(4),[["mm_autumn_tree","bo_mm_autumn_tree",("0","0")],["mm_autumn_tree1","bo_mm_autumn_tree1",("0","0")],["mm_autumn_tree3","bo_mm_autumn_tree3",("0","0")],["mm_autumn_tree2","bo_mm_autumn_tree2",("0","0")],["mm_autumn_tree4","bo_mm_autumn_tree4",("0","0")]]),
  ("mm_pine_copy",fkf_plain|fkf_plain_forest|fkf_tree|fkf_steppe|fkf_steppe_forest|density(4),[["mm_pine1","bo_mm_pine1",("0","0")],["mm_pine2","bo_mm_pine2",("0","0")],["mm_pine3","bo_mm_pine3",("0","0")],["mm_pine4","bo_mm_pine4",("0","0")],["mm_pine5","bo_mm_pine5",("0","0")],["mm_pine6","bo_mm_pine6",("0","0")],["mm_pine7","bo_mm_pine7",("0","0")]]),
  ("mm_winter_tree",fkf_tree|density(0),[["mm_winter_tree","bo_mm_winter_tree",("0","0")],["mm_winter_tree1","bo_mm_winter_tree1",("0","0")],["mm_winter_tree2","bo_mm_winter_tree2",("0","0")],["mm_winter_tree3","bo_mm_winter_tree3",("0","0")],["mm_winter_tree4","bo_mm_winter_tree4",("0","0")],["mm_winter_tree5","bo_mm_winter_tree5",("0","0")],["mm_winter_tree6","bo_mm_winter_tree6",("0","0")],["mm_winter_tree7","bo_mm_winter_tree7",("0","0")],["mm_winter_tree8","bo_mm_winter_tree8",("0","0")],["mm_winter_tree9","bo_mm_winter_tree9",("0","0")],["mm_winter_tree10","bo_mm_winter_tree10",("0","0")],["mm_winter_tree11","bo_mm_winter_tree11",("0","0")],["mm_winter_tree12","bo_mm_winter_tree12",("0","0")],["mm_winter_tree13","bo_mm_winter_tree13",("0","0")],["mm_winter_tree14","bo_mm_winter_tree14",("0","0")],["mm_winter_tree15","bo_mm_winter_tree15",("0","0")]]),
  ("mm_big_tree",fkf_tree|density(0),[["big_tree_mm","bo_big_tree_mm",("0","0")],["big_tree_mm1","bo_big_tree_mm1",("0","0")],["big_tree_mm2","bo_big_tree_mm2",("0","0")],["big_tree_mm3","bo_big_tree_mm3",("0","0")]]),
  ("mm_tree1",fkf_plain|fkf_plain_forest|fkf_tree|fkf_steppe|fkf_steppe_forest|density(4),[["mm_vegetation_tree1","bo_mm_vegetation_tree1",("0","0")],["mm_vegetation_tree2","bo_mm_vegetation_tree2",("0","0")],["mm_vegetation_tree3","bo_mm_vegetation_tree3",("0","0")],["mm_vegetation_tree4","bo_mm_vegetation_tree4",("0","0")],["mm_vegetation_tree5","bo_mm_vegetation_tree5",("0","0")],["mm_vegetation_tree6","bo_mm_vegetation_tree6",("0","0")],["mm_vegetation_tree7","bo_mm_vegetation_tree7",("0","0")],["mm_vegetation_tree8","bo_mm_vegetation_tree8",("0","0")],["mm_vegetation_tree9","bo_mm_vegetation_tree9",("0","0")],["mm_vegetation_tree10","bo_mm_vegetation_tree10",("0","0")],["mm_vegetation_tree11","bo_mm_vegetation_tree11",("0","0")],["mm_vegetation_tree12","bo_mm_vegetation_tree12",("0","0")],["mm_vegetation_tree14","bo_mm_vegetation_tree14",("0","0")],["mm_vegetation_tree15","bo_mm_vegetation_tree15",("0","0")]]),
  ("mm_tree2",fkf_plain|fkf_plain_forest|fkf_tree|fkf_steppe|fkf_steppe_forest|density(4),[["mm_vegetation_tree21","bo_mm_vegetation_tree1",("0","0")],["mm_vegetation_tree22","bo_mm_vegetation_tree2",("0","0")],["mm_vegetation_tree23","bo_mm_vegetation_tree3",("0","0")],["mm_vegetation_tree24","bo_mm_vegetation_tree4",("0","0")],["mm_vegetation_tree25","bo_mm_vegetation_tree5",("0","0")],["mm_vegetation_tree26","bo_mm_vegetation_tree6",("0","0")],["mm_vegetation_tree27","bo_mm_vegetation_tree7",("0","0")],["mm_vegetation_tree28","bo_mm_vegetation_tree8",("0","0")],["mm_vegetation_tree29","bo_mm_vegetation_tree9",("0","0")],["mm_vegetation_tree210","bo_mm_vegetation_tree10",("0","0")],["mm_vegetation_tree211","bo_mm_vegetation_tree11",("0","0")],["mm_vegetation_tree212","bo_mm_vegetation_tree12",("0","0")],["mm_vegetation_tree214","bo_mm_vegetation_tree14",("0","0")],["mm_vegetation_tree215","bo_mm_vegetation_tree15",("0","0")]]),
  ("mm_tree3",fkf_tree|density(4),[["mm_vegetation_tree31","bo_mm_vegetation_tree1",("0","0")],["mm_vegetation_tree32","bo_mm_vegetation_tree2",("0","0")],["mm_vegetation_tree33","bo_mm_vegetation_tree3",("0","0")],["mm_vegetation_tree34","bo_mm_vegetation_tree4",("0","0")],["mm_vegetation_tree35","bo_mm_vegetation_tree5",("0","0")],["mm_vegetation_tree36","bo_mm_vegetation_tree6",("0","0")],["mm_vegetation_tree37","bo_mm_vegetation_tree7",("0","0")],["mm_vegetation_tree38","bo_mm_vegetation_tree8",("0","0")],["mm_vegetation_tree39","bo_mm_vegetation_tree9",("0","0")],["mm_vegetation_tree310","bo_mm_vegetation_tree10",("0","0")],["mm_vegetation_tree311","bo_mm_vegetation_tree11",("0","0")],["mm_vegetation_tree312","bo_mm_vegetation_tree12",("0","0")],["mm_vegetation_tree314","bo_mm_vegetation_tree14",("0","0")],["mm_vegetation_tree315","bo_mm_vegetation_tree15",("0","0")]]),
  ("mm_tree7",fkf_tree|fkf_steppe|fkf_steppe_forest|density(4),[["mm_vegetation_tree71","bo_mm_vegetation_tree1",("0","0")],["mm_vegetation_tree72","bo_mm_vegetation_tree2",("0","0")],["mm_vegetation_tree73","bo_mm_vegetation_tree3",("0","0")],["mm_vegetation_tree74","bo_mm_vegetation_tree4",("0","0")],["mm_vegetation_tree75","bo_mm_vegetation_tree5",("0","0")],["mm_vegetation_tree76","bo_mm_vegetation_tree6",("0","0")],["mm_vegetation_tree77","bo_mm_vegetation_tree7",("0","0")],["mm_vegetation_tree78","bo_mm_vegetation_tree8",("0","0")],["mm_vegetation_tree79","bo_mm_vegetation_tree9",("0","0")],["mm_vegetation_tree710","bo_mm_vegetation_tree10",("0","0")],["mm_vegetation_tree711","bo_mm_vegetation_tree11",("0","0")],["mm_vegetation_tree712","bo_mm_vegetation_tree12",("0","0")],["mm_vegetation_tree714","bo_mm_vegetation_tree14",("0","0")],["mm_vegetation_tree715","bo_mm_vegetation_tree15",("0","0")]]),
  ("mm_tree8",fkf_plain|fkf_plain_forest|fkf_tree|density(4),[["mm_vegetation_tree81","bo_mm_vegetation_tree1",("0","0")],["mm_vegetation_tree82","bo_mm_vegetation_tree2",("0","0")],["mm_vegetation_tree83","bo_mm_vegetation_tree3",("0","0")],["mm_vegetation_tree84","bo_mm_vegetation_tree4",("0","0")],["mm_vegetation_tree85","bo_mm_vegetation_tree5",("0","0")],["mm_vegetation_tree86","bo_mm_vegetation_tree6",("0","0")],["mm_vegetation_tree87","bo_mm_vegetation_tree7",("0","0")],["mm_vegetation_tree88","bo_mm_vegetation_tree8",("0","0")],["mm_vegetation_tree89","bo_mm_vegetation_tree9",("0","0")],["mm_vegetation_tree810","bo_mm_vegetation_tree10",("0","0")],["mm_vegetation_tree811","bo_mm_vegetation_tree11",("0","0")],["mm_vegetation_tree812","bo_mm_vegetation_tree12",("0","0")],["mm_vegetation_tree814","bo_mm_vegetation_tree14",("0","0")],["mm_vegetation_tree815","bo_mm_vegetation_tree15",("0","0")]]),
  ("mm_tree9",fkf_tree|density(4),[["mm_vegetation_tree91","bo_mm_vegetation_tree1",("0","0")],["mm_vegetation_tree92","bo_mm_vegetation_tree2",("0","0")],["mm_vegetation_tree93","bo_mm_vegetation_tree3",("0","0")],["mm_vegetation_tree94","bo_mm_vegetation_tree4",("0","0")],["mm_vegetation_tree95","bo_mm_vegetation_tree5",("0","0")],["mm_vegetation_tree96","bo_mm_vegetation_tree6",("0","0")],["mm_vegetation_tree97","bo_mm_vegetation_tree7",("0","0")],["mm_vegetation_tree98","bo_mm_vegetation_tree8",("0","0")],["mm_vegetation_tree99","bo_mm_vegetation_tree9",("0","0")],["mm_vegetation_tree910","bo_mm_vegetation_tree10",("0","0")],["mm_vegetation_tree911","bo_mm_vegetation_tree11",("0","0")],["mm_vegetation_tree912","bo_mm_vegetation_tree12",("0","0")],["mm_vegetation_tree914","bo_mm_vegetation_tree14",("0","0")],["mm_vegetation_tree915","bo_mm_vegetation_tree15",("0","0")]]),
  ("mm_tree10",fkf_plain|fkf_plain_forest|fkf_tree|density(4),[["mm_vegetation_tree101","bo_mm_vegetation_tree1",("0","0")],["mm_vegetation_tree102","bo_mm_vegetation_tree2",("0","0")],["mm_vegetation_tree103","bo_mm_vegetation_tree3",("0","0")],["mm_vegetation_tree104","bo_mm_vegetation_tree4",("0","0")],["mm_vegetation_tree104","bo_mm_vegetation_tree4",("0","0")],["mm_vegetation_tree106","bo_mm_vegetation_tree6",("0","0")],["mm_vegetation_tree107","bo_mm_vegetation_tree7",("0","0")],["mm_vegetation_tree108","bo_mm_vegetation_tree8",("0","0")],["mm_vegetation_tree109","bo_mm_vegetation_tree9",("0","0")],["mm_vegetation_tree1010","bo_mm_vegetation_tree10",("0","0")],["mm_vegetation_tree1011","bo_mm_vegetation_tree11",("0","0")],["mm_vegetation_tree1012","bo_mm_vegetation_tree12",("0","0")],["mm_vegetation_tree1014","bo_mm_vegetation_tree14",("0","0")],["mm_vegetation_tree1015","bo_mm_vegetation_tree15",("0","0")]]),
  ("mm_tree11",fkf_plain|fkf_plain_forest|fkf_tree|density(4),[["mm_vegetation_tree111","bo_mm_vegetation_tree1",("0","0")],["mm_vegetation_tree112","bo_mm_vegetation_tree2",("0","0")],["mm_vegetation_tree113","bo_mm_vegetation_tree3",("0","0")],["mm_vegetation_tree114","bo_mm_vegetation_tree4",("0","0")],["mm_vegetation_tree114","bo_mm_vegetation_tree4",("0","0")],["mm_vegetation_tree116","bo_mm_vegetation_tree6",("0","0")],["mm_vegetation_tree117","bo_mm_vegetation_tree7",("0","0")],["mm_vegetation_tree118","bo_mm_vegetation_tree8",("0","0")],["mm_vegetation_tree119","bo_mm_vegetation_tree9",("0","0")],["mm_vegetation_tree1110","bo_mm_vegetation_tree10",("0","0")],["mm_vegetation_tree1111","bo_mm_vegetation_tree11",("0","0")],["mm_vegetation_tree1112","bo_mm_vegetation_tree12",("0","0")],["mm_vegetation_tree1114","bo_mm_vegetation_tree14",("0","0")],["mm_vegetation_tree1115","bo_mm_vegetation_tree15",("0","0")]]),
  ("mm_northern2",fkf_tree|density(0),[["mm_northern_tree3","bo_mm_northern_tree3",("0","0")],["mm_northern_tree4","bo_mm_northern_tree4",("0","0")]]),
  ("mm_random_stuff",fkf_plain|fkf_align_with_ground|fkf_plain_forest|fkf_steppe_forest|fkf_rock|density(4),[["mm_random_plant2","bo_mm_random_plant2"],["mm_random_plant3","bo_mm_random_plant2"],["mm_random_plant4","bo_mm_random_plant2"],["mm_random_plant5","bo_mm_random_plant2"],["mm_random_plant6","bo_mm_random_plant6"],["mm_random_plant7","bo_mm_random_plant6"],["mm_random_plant18","bo_mm_random_plant6"],["mm_random_plant9","bo_mm_random_plant9"],["mm_random_plant8","bo_mm_random_plant9"],["mm_random_plant10","bo_mm_random_plant14"],["mm_random_plant11","bo_mm_random_plant14"],["mm_random_plant12","bo_mm_random_plant14"],["mm_random_plant14","bo_mm_random_plant14"],["mm_random_plant15","bo_mm_random_plant17"],["mm_random_plant16","bo_mm_random_plant17"],["mm_random_plant17","bo_mm_random_plant17"]]),
  ("mm_palm_tree",fkf_desert_forest|fkf_tree|density(1),[["palmb_7","bo_palmb_7",("0","0")],["palmb_8","bo_palmb_8",("0","0")],["palmb_9","bo_palmb_9",("0","0")],["palmb_10","bo_palmb_10",("0","0")],["palmb_11","bo_palmb_11",("0","0")],["palmb_12","bo_palmb_12",("0","0")]]),
  # patch1115 bug fix 42/2 end

  ("small_rock_mm_desert",fkf_align_with_ground|fkf_desert|fkf_desert_forest|fkf_realtime_ligting|fkf_rock|density(6),[["mmrock_c","bo_rock_c"],["mmrock_d","bo_rock_d"],["mmrock_e","bo_rock_e"],["mmrock_f","bo_rock_f"],["mmrock_g","bo_rock_g"],["mmrock_h","bo_rock_h"],["mmrock_i","bo_rock_i"],["mmrock_k","bo_rock_k"]]),
  ("mm_rock_desert",fkf_align_with_ground|fkf_desert|fkf_desert_forest|fkf_realtime_ligting|fkf_rock|density(7),[["mmrock1","bo_rock1"],["mmrock2","bo_rock2"],["mmrock3","bo_rock3"],["mmrock4","bo_rock4"],["mmrock5","bo_rock5"],["mmrock7","bo_rock7"]]),  # patch1115 bug fix 42/3

  ("mm_flowers1",fkf_plain|fkf_steppe|fkf_steppe_forest|fkf_align_with_ground|density(20),[["grass_bush_amm","0"],["grass_bush_bmm","0"]]),
  ("mm_flowers",fkf_plain|fkf_plain_forest|fkf_steppe_forest|fkf_align_with_ground|density(20),[["grass_bush_cmm","0"],["grass_bush_c2mm","0"],["grass_bush_c3mm","0"],["grass_bush_dmm","0"]]),
  ("mm_flowers2",fkf_plain|fkf_plain_forest|fkf_steppe_forest|fkf_align_with_ground|density(20),[["grass_bush_emm","0"],["grass_bush_fmm","0"],["grass_bush_gmm","0"],["grass_bush_hmm","0"],["grass_bush_imm","0"],["grass_bush_jmm","0"],["grass_bush_kmm","0"],["grass_bush_lmm","0"],["grass_bush_mmm","0"]]),
  ("mm_mushrooms",fkf_plain|fkf_plain_forest|fkf_steppe_forest|fkf_align_with_ground|density(0),[["mm_mushrooms2","0"],["mm_mushrooms","0"]]),
  ("mm_bush_green",fkf_plain|fkf_plain_forest|fkf_align_with_ground|density(20),[["mm_bush","0"],["mm_bush2","0"],["mm_bush3","0"],["mm_bush4","0"],["mm_bush5","0"],["mm_bush6","0"],["mm_bush7","0"]]),
  ("mm_bush_orange",fkf_plain|fkf_plain_forest|fkf_steppe_forest|fkf_align_with_ground|density(20),[["mm_bush_new","0"],["mm_bush_new2","0"],["mm_bush_new3","0"],["mm_bush_new4","0"],["mm_bush_new5","0"],["mm_bush_new6","0"],["mm_bush_new7","0"]]),
  ("mm_giant_bush",fkf_plain|fkf_plain_forest|fkf_align_with_ground|density(20),[["mm_giant_bush","0"],["mm_giant_bush2","0"],["mm_giant_bush3","0"],["mm_giant_bush4","0"],["mm_giant_bush5","0"],["mm_giant_bush6","0"],["mm_giant_bush7","0"]]),
  ("mm_old_bush",fkf_plain|fkf_plain_forest|fkf_steppe_forest|fkf_align_with_ground|density(20),[["mm_giant_bush_new","0"],["mm_giant_bush_new2","0"],["mm_giant_bush_new3","0"],["mm_giant_bush_new4","0"],["mm_giant_bush_new5","0"],["mm_giant_bush_new6","0"],["mm_giant_bush_new7","0"]]),
  ("mm_old_bush1",fkf_plain|fkf_plain_forest|fkf_align_with_ground|density(20),[["mm_old_bush","0"],["mm_old_bush2","0"],["mm_old_bush3","0"],["mm_old_bush4","0"],["mm_old_bush5","0"],["mm_old_bush6","0"],["mm_old_bush7","0"]]),
  ("mm_flower_bush",fkf_plain|fkf_align_with_ground|density(20),[["bush_flower","0"],["bush_flower1","0"],["bush_flower2","0"],["bush_flower3","0"],["bush_flower4","0"],["bush_flower5","0"],["bush_flower6","0"],["bush_flower7","0"],["bush_flower8","0"],["bush_flower9","0"],["bush_flower11","0"],["bush_flower12","0"],["bush_flower13","0"],["bush_flower14","0"],["bush_flower15","0"],["bush_flower16","0"],["bush_flower17","0"],["bush_flower18","0"],["bush_flower19","0"],["bush_flower20","0"]]),
  ("mm_bush_green_new",fkf_plain|fkf_plain_forest|fkf_align_with_ground|density(20),[["bush_new_green1","0"],["bush_new_green2","0"],["bush_new_green3","0"],["bush_new_green4","0"],["bush_new_green5","0"],["bush_new_green6","0"],["bush_new_green7","0"]]),
  ("mm_bush_winter",fkf_snow|fkf_snow_forest|fkf_align_with_ground|density(20),[["mm_bush_winter","0"],["mm_bush_winter1","0"],["mm_bush_winter2","0"],["mm_bush_winter3","0"],["mm_bush_winter4","0"],["mm_bush_winter5","0"],["mm_bush_winter6","0"],["mm_bush_winter7","0"],["mm_bush_winter8","0"],["mm_bush_winter9","0"],["mm_bush_winter10","0"]]),
  ("mm_bush_winter2",fkf_align_with_ground|density(0),[["mm_bush_winter14","0"],["mm_bush_winter15","0"],["mm_bush_winter16","0"],["mm_bush_winter17","0"]]),
  ("mm_roses",fkf_align_with_ground|density(0),[["roses","0"]]),

  ("plant_forest4",fkf_align_with_ground|density(0),[["mm_bush_new_lot1","0"],["mm_bush_new_lot2","0"],["mm_bush_new_lot3","0"],["mm_bush_new_lot4","0"],["mm_bush_new_lot5","0"]]),

  ("mm_wheat",fkf_align_with_ground|density(0),[["mm_wheat","0"],["mm_wheat1","0"],["mm_wheat2","0"],["mm_wheat3","0"]]),
  ("mm_hedge1",fkf_align_with_ground|density(0),[["mm_hedge1","0"],["mm_hedge2","0"],["mm_hedge3","0"]]),
  ("mm_hedge2",fkf_align_with_ground|density(0),[["mm_hedge11","0"],["mm_hedge12","0"],["mm_hedge13","0"]]),
  ("mm_hedge3",fkf_align_with_ground|density(0),[["mm_hedge21","0"],["mm_hedge22","0"],["mm_hedge23","0"]]),
  ("mm_hedge4",fkf_align_with_ground|density(0),[["mm_hedge31","0"],["mm_hedge32","0"],["mm_hedge33","0"]]),
  ("mm_hedge5",fkf_align_with_ground|density(0),[["mm_hedge41","0"],["mm_hedge42","0"],["mm_hedge43","0"]]),
  ("mm_hedge6",fkf_align_with_ground|density(0),[["mm_hedge51","0"],["mm_hedge52","0"],["mm_hedge53","0"]]),
  ("mm_hedge7",fkf_align_with_ground|density(0),[["mm_hedge61","0"],["mm_hedge62","0"],["mm_hedge63","0"]]),
  ("mm_hedge8",fkf_align_with_ground|density(0),[["mm_hedge71","0"],["mm_hedge72","0"],["mm_hedge73","0"]]),
  ("mm_hedge9",fkf_align_with_ground|density(0),[["mm_hedge81","0"],["mm_hedge82","0"],["mm_hedge83","0"]]),
  ("mm_hedge10",fkf_align_with_ground|density(0),[["mm_hedge91","0"],["mm_hedge92","0"],["mm_hedge93","0"]]),
  ("mm_hedge11",fkf_align_with_ground|density(0),[["mm_hedge101","0"],["mm_hedge102","0"],["mm_hedge103","0"]]),
  ("mm_desert",fkf_align_with_ground|fkf_desert|density(10),[["mm_bush_desert1","0"],["mm_bush_desert2","0"],["mm_bush_desert3","0"],["mm_bush_desert4","0"],["mm_bush_desert5","0"],["mm_bush_desert6","0"],["mm_bush_desert7","0"]]),
  ("mm_desert_forest_plants",fkf_align_with_ground|fkf_guarantee|fkf_desert_forest|density(2),[["spiky_plantmm","0"],["spiky_plantmm2","0"],["spiky_plantmm3","0"],["spiky_plantmm4","0"],["spiky_plantmm5","0"],["spiky_plantmm6","0"],]),
  ("mm_cattail",fkf_align_with_ground|density(0),[["cattail1","0"],["cattail2","0"],["cattail3","0"],["cattail4","0"],["cattail5","0"],["cattail6","0"],["cattail7","0"]]),
  ("mm_lilly",fkf_align_with_ground|density(0),[["lilly1","0"]]),

]


def save_fauna_kinds():
  file = open("./flora_kinds.txt","w")
  file.write("%d\n"%len(fauna_kinds))
  for fauna_kind in fauna_kinds:
    meshes_list = fauna_kind[2]
    file.write("%s %d %d\n"%(fauna_kind[0], (dword_mask & fauna_kind[1]), len(meshes_list)))
    for m in meshes_list:
      file.write(" %s "%(m[0]))
      if (len(m) > 1):
        file.write(" %s\n"%(m[1]))
      else:
        file.write(" 0\n")
      if ( fauna_kind[1] & (fkf_tree|fkf_speedtree) ):  #if this fails make sure that you have entered the alternative tree definition (NOT FUNCTIONAL in Warband)
        speedtree_alternative = m[2]
        file.write(" %s %s\n"%(speedtree_alternative[0], speedtree_alternative[1]))
    if ( fauna_kind[1] & fkf_has_colony_props ):
      file.write(" %s %s\n"%(fauna_kind[3], fauna_kind[4]))
  file.close()

def two_to_pow(x):
  result = 1
  for i in xrange(x):
    result = result * 2
  return result

fauna_mask = 0x80000000000000000000000000000000
low_fauna_mask =             0x8000000000000000
def save_python_header():
  file = open("./fauna_codes.py","w")
  for i_fauna_kind in xrange(len(fauna_kinds)):
    file.write("%s_1 = 0x"%(fauna_kinds[i_fauna_kind][0]))
    file.write("%x\n"%(fauna_mask | two_to_pow(i_fauna_kind)))
    file.write("%s_2 = 0x"%(fauna_kinds[i_fauna_kind][0]))
    file.write("%x\n"%(fauna_mask | ((low_fauna_mask|two_to_pow(i_fauna_kind)) << 64)))
    file.write("%s_3 = 0x"%(fauna_kinds[i_fauna_kind][0]))
    file.write("%x\n"%(fauna_mask | ((low_fauna_mask|two_to_pow(i_fauna_kind)) << 64) | two_to_pow(i_fauna_kind)))
  file.close()

print "Exporting flora data..."
save_fauna_kinds()
