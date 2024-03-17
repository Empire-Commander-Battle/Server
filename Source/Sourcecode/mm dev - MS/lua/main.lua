-- LOG
-- SCRIPTS
script_get_custom_log = game.getScriptNo("get_custom_log")
script_get_dump = game.getScriptNo("get_dump")
script_get_multiplayer_game_type = game.getScriptNo("get_multiplayer_game_type")
-- END SCRIPTS

-- CUSTOM LOG
custom_log = io.open("custom_log.txt", "a")
-- END CUSTOM LOG

function log_date()
   return os.date("%Y.%m.%d %X")
end

function log_write(str)
   custom_log:write(string.format("[%s]: %s\n", log_date(), str))
   custom_log:flush()
end

function on_agent_spawn()
   -- result in reg0
   game.call_script(script_get_custom_log)
   local custom_log_enabled = game.reg[0]

   if custom_log_enabled == 0 then
	  return
   end

   local agent, err = game.store_trigger_param(0, 1)

   local team, err = game.agent_get_team(0, agent)
   local troop, err = game.agent_get_troop_id(0, agent)

   local player, err = game.agent_get_player_id(0, agent)
   if player == -1 then
	  -- BOT

	  local group, err = game.agent_get_group(0, agent)
	  log_write(string.format("action: 'spawned bot' troop: '%s' team: '%s' agent: '%s' group_leader: '%s'", troop, team, agent, group))
   else
	  -- PLAYER
	  -- result in s0
	  game.str_store_player_username(game.const.s0, player)
	  local username = game.sreg[0]

	  log_write(string.format("action: 'spawned player' username: '%s' troop: '%s' team: '%s' agent: '%s' player: '%s'", username, troop, team, agent, player))
   end
end

function on_agent_killed_or_wounded()
   game.display_message("DEBUG KILLED WOUNDED")
   -- result in reg0
   game.call_script(script_get_custom_log)
   local custom_log_enabled = game.reg[0]

   if custom_log_enabled == 0 then
	  return
   end

   local agent, err = game.store_trigger_param(0, 1)
   local dealer_agent, err = game.store_trigger_param(0, 2)
   local wounded, err = game.store_trigger_param(0, 3)

   if wounded == 1 then
	  log_write(string.format("action: 'wounded agent' agent: '%s' dealer_agent: '%s'", agent, dealer_agent))
   else
	  log_write(string.format("action: 'killed agent' agent: '%s' killer: '%s'", agent, dealer_agent))
   end
end

function on_agent_start_reloading()
   -- result in reg0
   game.call_script(script_get_custom_log)
   local custom_log_enabled = game.reg[0]

   if custom_log_enabled == 0 then
	  return
   end

   local agent, err = game.store_trigger_param(0, 1)

   log_write(string.format("action: 'agent started reloading' agent: %s", agent))
end

function on_agent_end_reloading()
   -- result in reg0
   game.call_script(script_get_custom_log)
   local custom_log_enabled = game.reg[0]

   if custom_log_enabled == 0 then
	  return
   end

   local agent, err = game.store_trigger_param(0, 1)

   log_write(string.format("action: 'agent ended reloading' agent: %s", agent))
end

function on_missile_hit()
   -- result in reg0
   game.call_script(script_get_custom_log)
   local custom_log_enabled = game.reg[0]

   if custom_log_enabled == 0 then
	  return
   end

   local agent, err = game.store_trigger_param(0, 1)
   local hit_position = game.preg[0]

   log_write(string.format("action: 'missile hit' agent: %s hit_position: %s", agent, hit_position))
end

function on_mission_start()
   -- result in reg0
   game.call_script(script_get_custom_log)
   local custom_log_enabled = game.reg[0]

   if custom_log_enabled == 0 then
	  return
   end

   game.call_script(script_get_multiplayer_game_type)
   local game_type = game.reg[0]

   log_write(string.format('Started mission game type %s', game_type))
end

function dump()
   -- result in reg0
   game.call_script(script_get_custom_log)
   local custom_log_enabled = game.reg[0]

   if custom_log_enabled == 0 then
	  return
   end

   -- result in reg0
   game.call_script(script_get_dump)
   local dump_enabled = game.reg[0]

   -- game.display_message(string.format("DUMP %s", dump_enabled))

   if dump_enabled == 0 then
	  return
   end

   DUMP_STRING = ''
   for agent in game.agentsI() do
	  game.agent_get_position(game.const.pos0, agent)
	  local pos = game.preg[0]

	  local troop, err = game.agent_get_troop_id(0, agent)
	  local team, err = game.agent_get_team(0, agent)

	  DUMP_STRING = DUMP_STRING .. string.format("|A:%s P:(%s, %s, %s) TT:%s TE:%s|", agent, pos.o.x, pos.o.y, pos.o.z, troop, team)
   end

   log_write(string.format("action: 'dump' data: '%s'", DUMP_STRING))
end


-- LOG SETUP
log_write("Server started")

game.addTrigger("mst_multiplayer_cb", game.const.ti_on_agent_spawn, 0, 0, on_agent_spawn)
game.addTrigger("mst_multiplayer_cb", game.const.ti_on_agent_killed_or_wounded, 0, 0, on_agent_killed_or_wounded)
game.addTrigger("mst_multiplayer_cb", game.const.ti_on_agent_start_reloading, 0, 0, on_agent_start_reloading)
game.addTrigger("mst_multiplayer_cb", game.const.ti_on_agent_end_reloading, 0, 0, on_agent_end_reloading)
game.addTrigger("mst_multiplayer_cb", game.const.ti_on_missile_hit, 0, 0, on_missile_hit)
game.addTrigger("mst_multiplayer_cb", game.const.ti_after_mission_start, 0, 0, on_mission_start)
game.addTrigger("mst_multiplayer_cb", 10, 0, 0, dump)
-- END LOG SETUP
-- END LOG

-- FORMATIONS
-- SCRIPTS
script_player_unit_get_position = game.getScriptNo("player_unit_get_position")
script_player_unit_get_spacing = game.getScriptNo("player_unit_get_spacing")
script_player_unit_get_rows = game.getScriptNo("player_unit_get_rows")
-- END SCRIPTS

-- VECTOR2
vector2 = {x = 0, y = 0}

function vector2:create(x, y)
   return {parent = self, x = x, y = y}
end

function vector2_from_vector3(v3)
   return vector2:create(v3.x, v3.y)
end

function vector2_add(a, b)
   return vector2:create(a.x + b.x, a.y + b.y)
end

function vector2_sub(a, b)
   return vector2:create(a.x - b.x, a.y - b.y)
end

function vector2_smul(a, s)
   return vector2:create(a.x*s, a.y*s)
end

function vector2_vec_distance(a, b)
   if b.x == 0 then
	  return a.y/b.y
   else
	  return a.x/b.x
   end
end
-- END VECTOR2

function iter_player_unit(player)
   local agent_iter = game.agentsI()
   return function ()
	  while true do
		 ::cont::
		 local agent = agent_iter()

		 if agent == nil then
			return
		 end

		 if game.agent_is_active(agent) and
			game.agent_is_human(agent) and
			game.agent_is_alive(agent) and
			game.agent_is_non_player(agent)
		 then

			local group = game.agent_get_group(agent)
			if group ~= player then
			   goto cont
			end

			if not game.agent_slot_eq(agent, game.const.slot_agent_is_running_away, 0) then
			   goto cont
			end

			return agent
		 end
	  end
   end
end

-- FORMATION VARS
crouch_dict = {}
-- END FORMATION VARS

-- Functions need to be written in camel case to be callable from warband scripts
function playerUnitForm(player)
   game.call_script(script_player_unit_get_spacing, player)
   local spacing = game.reg[0]/100
   game.display_message(string.format("spacing: %s", spacing))

   game.call_script(script_player_unit_get_position, player)
   local w_pos = game.preg[0]
   local pos = vector2_from_vector3(w_pos.o)

   local forward = vector2_from_vector3(w_pos.rot.f)
   local left = vector2:create(-forward.y, forward.x)

   local cpos = vector2_sub(pos, vector2_smul(forward, spacing))

   local A = forward.y
   local B = -forward.x

   local projection = {}

   for agent in iter_player_unit(player) do
	  game.agent_get_position(game.const.pos0, agent)

	  local w_apos = game.preg[0]
	  local apos = vector2_from_vector3(w_apos.o)

	  local p_x = (A*A*apos.x + B*B*cpos.x + A*B*(apos.y - cpos.y))/(A*A + B*B)
	  local p_y = (A*A*cpos.y + B*B*apos.y + A*B*(apos.x - cpos.x))/(A*A + B*B)

	  local kpos = vector2:create(p_x, p_y)

	  table.insert(projection,
				   {agent = agent,
					w_pos = w_apos,
					kpos = kpos,
					dist = vector2_vec_distance(vector2_sub(kpos, cpos), left)})

	  -- game.agent_set_scripted_destination(agent, game.const.pos0, 1)

	  -- game.display_message(string.format("(%s, %s)", game.preg[0].o.x, game.preg[0].o.y))
	  -- game.display_message(string.format("(%s, %s)", p_x, p_y))
   end

   table.sort(projection,
			  function (a, b) return a.dist < b.dist end)

   game.call_script(script_player_unit_get_rows, player)
   local rows = game.reg[0]

   local formation = {}
   local tmp_arr = {}
   for k, v in pairs(projection) do
	  v.dist = vector2_vec_distance(vector2_sub(vector2_from_vector3(v.w_pos.o), v.kpos), forward)

	  table.insert(tmp_arr, v)
	  if #tmp_arr == rows then
		 table.sort(tmp_arr,
					function (a, b) return a.dist > b.dist end)
		 table.insert(formation, tmp_arr)
		 tmp_arr = {}
	  end
   end

   if #tmp_arr ~= 0 then
	  table.sort(tmp_arr,
				 function (a, b) return a.dist > b.dist end)
	  table.insert(formation, tmp_arr)
	  tmp_arr = {}
   end

   game.display_message(string.format("len %s spacing %s", #formation, spacing))

   local crouching_list = {}
   -- crouch_dict[player]
   -- if crouching_list ~= nil then
   --	  for _, agent in pairs(crouching_list) do
   --		 game.agent_set_slot(agent, game.const.slot_agent_crouching, 0)
   --	  end
   -- end

   local move_x = vector2_smul(left, spacing)
   local move_y = vector2_smul(forward, -spacing)

   for rank_index, row in pairs(formation) do
	  for row_index, v in pairs(row) do
		 -- game.display_message(string.format("RANK %s ROW %s", rank_index, row_index))

		 game.agent_ai_set_can_crouch(v.agent, 0)

		 -- if row_index == 1 then
		 --		table.insert(crouching_list, v.agent)
		 --		game.agent_ai_set_can_crouch(v.agent, 1)
		 -- else
		 --		game.agent_ai_set_can_crouch(v.agent, 0)
		 -- end

		 local dest = vector2_add(cpos, vector2_smul(move_x, rank_index - #formation/2 - 0.5))
		 dest = vector2_add(dest, vector2_smul(move_y, row_index - 1))

		 local pos = game.pos.new()
		 pos.o.x = dest.x
		 pos.o.y = dest.y

		 -- game.display_message(string.format("%s %s", dest.x, dest.y))

		 game.preg[0] = pos

		 game.agent_set_scripted_destination(v.agent, game.const.pos0, 1)
	  end
   end

   -- for _, agent in pairs(crouching_list) do
   --	  game.agent_set_slot(agent, game.const.slot_agent_crouching, 1)
   -- end

   crouch_dict[player] = crouching_list
end

function ensure_crouching()
   for player, agent_list in pairs(crouch_dict) do
	  for _, agent in pairs(agent_list) do
		 if game.agent_is_active(agent) and
			game.agent_is_alive(agent)
		 then
			-- game.agent_ai_set_can_crouch(agent, 1)
			-- game.agent_set_crouch_mode(agent, 1)
			-- game.display_message(string.format("%s", agent))

			-- game.agent_set_wielded_item(agent, -1)
			-- game.agent_set_animation(agent, "anim_surrender", 1)
		 end
	  end
   end
end

function formation_player_exit()
   local player, err = game.store_trigger_param(0, 1)
   crouch_dict[player] = nil
end

function formation_agent_killed()
   local agent, err = game.store_trigger_param(0, 1)
   local wounded, err = game.store_trigger_param(0, 2)

   if wounded then
	  return
   end

   local player = game.agent_get_group(agent)
   local agent_list = crouch_dict[player]

   for index, agent_in_list in pairs(agent_list) do
	  if agent_in_list == agent then
		 table.remove(agent_list, index)
		 return
	  end
   end
end

-- FORMATION SETUP
-- game.addTrigger("mst_multiplayer_cb", 5, 0, 0, ensure_crouching)
-- game.addTrigger("mst_multiplayer_cb", game.const.ti_on_player_exit, 0, 0, formation_player_exit)
-- game.addTrigger("mst_multiplayer_cb", game.const.ti_on_agent_killed_or_wounded, 0, 0, formation_agent_killed)
-- END FORMATION SETUP
-- END FORMATIONS
