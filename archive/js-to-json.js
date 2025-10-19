#!/usr/bin/env node

const fs = require('fs');
const vm = require('vm');

// Check if file path is provided
if (process.argv.length < 3) {
    console.error('Usage: node js-to-json.js <path-to-js-file>');
    process.exit(1);
}

const filePath = process.argv[2];

// Check if file exists
if (!fs.existsSync(filePath)) {
    console.error(`Error: File not found: ${filePath}`);
    process.exit(1);
}

try {
    // Read the JS file
    const jsContent = fs.readFileSync(filePath, 'utf8');
    
    // Create a sandbox context
    const sandbox = {};
    
    // Execute the JS code in the sandbox
    vm.createContext(sandbox);
    vm.runInContext(jsContent, sandbox);
    
    console.log(sandbox)

    // Output to stdout
    console.log(JSON.stringify(sandbox.json, null, 2));
    
} catch (error) {
    console.error(error);
    process.exit(1);
}