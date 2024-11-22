import jwt from "jsonwebtoken";

const createAccessToken = (paylod) => {
    return new Promise((resolve, reject) => {
        jwt.sign(paylod, "xyz123", {expiresIn: "id" },
        (err, token) => {
            if (err) reject(err);
            resolve(token);
        });

    });

};

export { createAccessToken };