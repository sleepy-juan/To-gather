import React from 'react';

const Register = ({match}) => {
    return (
        <div>
            <h2>{match.params.name}</h2>
        </div>
    );
};

export default Register;