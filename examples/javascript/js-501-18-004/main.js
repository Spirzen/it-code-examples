const createValidator = (rules) => (data) => {
    const errors = [];
    for (const [field, rule] of Object.entries(rules)) {
        if (!rule(data[field])) {
            errors.push(`Поле "${field}" не прошло валидацию.`);
        }
    }
    return errors.length === 0 ? null : errors;
};

const validateUser = createValidator({
    email: (v) => /\S+@\S+\.\S+/.test(v),
    age: (v) => v >= 18 && v < 120
});
