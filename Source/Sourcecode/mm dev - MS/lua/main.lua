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
	  log_write(string.format("action: 'spawned bot' troop: '%s' team: '%s' agent: '%s'", troop, team, agent))
   else
	  -- PLAYER
	  -- result in s0
	  game.str_store_player_username(game.const.s0, player)
	  local username = game.sreg[0]

	  log_write(string.format("action: 'spawned player' username: '%s' troop: '%s' team: '%s' agent: '%s'", username, troop, team, agent))
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

   log_write(string.format("action: 'missle hit' agent: %s hit_position: %s", agent, hit_position))
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

   game.display_message(string.format("DUMP %s", dump_enabled))

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

log_write("Server started")

game.addTrigger("mst_multiplayer_cb", game.const.ti_on_agent_spawn, 0, 0, on_agent_spawn)
game.addTrigger("mst_multiplayer_cb", game.const.ti_on_agent_killed_or_wounded, 0, 0, on_agent_killed_or_wounded)
game.addTrigger("mst_multiplayer_cb", game.const.ti_on_agent_start_reloading, 0, 0, on_agent_start_reloading)
game.addTrigger("mst_multiplayer_cb", game.const.ti_on_agent_end_reloading, 0, 0, on_agent_end_reloading)
game.addTrigger("mst_multiplayer_cb", game.const.ti_on_missile_hit, 0, 0, on_missile_hit)
game.addTrigger("mst_multiplayer_cb", game.const.ti_after_mission_start, 0, 0, on_mission_start)
game.addTrigger("mst_multiplayer_cb", 10, 0, 0, dump)
