export const state = () => ({
    runners: []
})

export const getters = {
    runners(state) {
        return state.runners
    },
    runners_counter: (state) => {
        return state.runners.length
    }
}

export const mutations = {
    SET_RUNNERS(state, MarketItems) {
        state.runners = MarketItems
    },
    REMOVE_RUNNERS(state, MarketItems) {
        state.runners = state.runners.filter(el => el.id !== MarketItems.id)
    },
    ADD_RUNNERS(state, MarketItems) {
        state.runners.unshift(MarketItems)
    }
}

export const actions = {
    async getRunners(context) {
        const res = await this.$axios.get('api/runners')
        if (!res.error) {
            context.commit("SET_RUNNERS", res.data)
        } else {
            context.commit("SET_RUNNERS", [])
        }
    },
    deleteRunnersItem(context, RunnersId) {
        return this.$axios.delete(`api/runners${RunnersId}`)
            .then(response => context.commit('REMOVE_RUNNERS', response.data)).catch(function (e) {
                throw e
            })
    },

    CreateRunners(context, payload) {
        return this.$axios.post(`api/runners`, payload).then(response => context.commit('ADD_RUNNERS', response.data))
    }
}

