-- -- SCRIPTS

-- script_player_unit_clear_scripted_mode = game.getScriptNo("player_unit_clear_scripted_mode")
-- script_player_unit_set_status = game.getScriptNo("player_unit_set_status")

-- -- END SCRIPTS

-- function player_joined()
--    game.display_message("PLAYER JOINED")
-- end

-- function order_issued()
--    -- it fails the first time that it is called for some reason....
--    local order, err = game.store_trigger_param(0, 1)
--    local player_agent, err = game.store_trigger_param(0, 2)

--    -- game.display_message(string.format("PLAYER AGENT %s", player_agent))

--    local player, err = game.agent_get_player_id(0, player_agent)
--    local active, err = game.player_is_active(player)
--    if not active then
--       return
--    end

--    game.display_message(string.format("ERR %s", err))
--    game.display_message(string.format("ORDER %s BY %s", order, player))
--    game.display_message(string.format("TEST1 %s", script_player_unit_clear_scripted_mode))
--    game.display_message(string.format("TEST2 %s", script_player_unit_set_status))
--    game.display_message(string.format("TEST3 %s", game.const.grc_everyone))
--    game.display_message(string.format("TEST4 %s", game.const.mordr_use_melee_weapons))
--    game.display_message(string.format("TEST5 %s", game.const.status_moving))

--    if order == game.const.mordr_charge then
--       game.display_message("CHARGE ORDER")

--       game.display_message(string.format("PLAYER %s", player))
--       game.call_script("script_player_unit_clear_scripted_mode", player)
--       game.display_message("TEST6")
--       game.call_script("script_player_unit_set_status", player, game.const.status_moving)
--       game.display_message("TEST7")

--       game.team_give_order(player, game.const.grc_everyone, game.const.mordr_use_melee_weapons)
--       game.set_show_messages(1)
--    end
-- end

-- game.addTrigger("mst_multiplayer_cb", game.const.ti_on_order_issued, 0, 0, order_issued)
-- game.addTrigger("mst_multiplayer_cb", game.const.ti_server_player_joined, 0, 0, player_joined)

-- p_data_rotation = 0
-- pu_data = {}

-- function p_data_get(player)
--    local p_data = pu_data[player]

--    if p_data == nil then
--       p_data = {
--	 p_data_rotation: 1
--       }

--       pu_data[player] = p_data
--    end

--    return p_data
-- end

-- function pu_get_rotation_mode(player)
--    local p_data = p_data_get(player)

--    game.display_message(string.format("PLAYER %s", player))

--    return 1
--    return p_data[p_data_rotation]
-- end


-- function pu_disable_rotation_mode(player)
--    local p_data = p_data_get(player)
--    p_data[p_data_rotation] = 0
-- end

-- function pu_enable_rotation_mode(player)
--    local p_data = p_data_get(player)
--    p_data[p_data_rotation] = 1
-- end

positions = {}

function player_unit_set_position(player)
   positions[player] = game.preg0

   game.display_message("DEBUG0")
end

function player_unit_get_position(player)
   tmp = positions[player]

   game.display_message("DEBUG1")

   if tmp ~= nil then
	  game.preg0 = positions[player]
   else
	  agent = game.player_get_agent_id(0, player)
	  game.preg0 = game.agent_get_position(0, agent),
   end
end
