export const state = () => ({
    markets: []
})

export const getters = {
    markets(state) {
        return state.markets
    },
    runners_counter: (state) => {
        return state.markets.length
    }
}

export const mutations = {
    SET_MARKETS(state, MarketItems) {
        state.markets = MarketItems
    },
    REMOVE_MARKETS(state, MarketItems) {
        state.markets = state.markets.filter(el => el.id !== MarketItems.id)
    },
    ADD_MARKETS(state, MarketItems) {
        state.markets.unshift(MarketItems)
    }
}

export const actions = {
    async getMarkets(context) {
        const res = await this.$axios.get('api/markets')
        if (!res.error) {
            context.commit("SET_MARKETS", res.data)
        } else {
            context.commit("SET_MARKETS", [])
        }
    },
    deleteMarketsItem(context, MarketsId) {
        return this.$axios.delete(`api/markets${MarketsId}`)
            .then(response => context.commit('REMOVE_MARKETS', response.data)).catch(function (e) {
                throw e
            })
    },

    CreateMarkets(context, payload) {
        return this.$axios.post(`api/markets`, payload).then(response => context.commit('ADD_MARKETS', response.data))
    }
}

