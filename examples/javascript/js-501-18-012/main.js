function updateNestedProperty(obj, path, value) {
    const keys = path.split('.');
    const result = { ...obj };
    let current = result;
    
    for (let i = 0; i < keys.length - 1; i++) {
        current[keys[i]] = { ...current[keys[i]] };
        current = current[keys[i]];
    }
    
    current[keys[keys.length - 1]] = value;
    return result;
}

const state = {
    user: {
        profile: {
            name: "Джон",
            settings: {
                theme: "light"
            }
        }
    }
};

const newState = updateNestedProperty(state, "user.profile.settings.theme", "dark");

console.log(state.user.profile.settings.theme); // "light" - оригинал не изменился
console.log(newState.user.profile.settings.theme); // "dark" - новая версия
