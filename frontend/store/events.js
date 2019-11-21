

export const state = () => ({
    events: []
})

export const getters = {
    events(state) {
        return state.events
    },
    events_counter: (state) => {
        return state.events.length
    }
}

export const mutations = {
    SET_EVENTS(state, EventItems) {
        state.events = EventItems
    },
    REMOVE_EVENTS(state, EventItems) {
        state.events = state.events.filter(el => el.id !== EventItems.id)
    },
    ADD_EVENTS(state, EventItems) {
        state.events.unshift(EventItems)
    }
}

export const actions = {
    async getEvents(context, app) {
        const res = await  app.$axios.get('api/events')
        if (!res.error) {
            context.commit("SET_EVENTS", res.data)
        } else {
            context.commit("SET_EVENTS", [])
        }
    },
    deleteEventsItem(context, EventId, app) {
        return app.$axios.delete(`api/events${EventId}`)
            .then(response => context.commit('REMOVE_EVENTS', response.data)).catch(function (e) {
                throw e
            })
    },

    CreateEvents(context, payload, app) {
        return  app.$axios.post(`api/events`, payload).then(response => context.commit('ADD_EVENTS', response.data))
    }
}

