"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const bin_1 = require("../bin/bin");
const utils_1 = require("../utils/utils");
/**
 * The most performant way to instantiate sha1 functionality. To avoid
 * using Node.js or DOM-specific APIs, you can use `instantiateSha1`.
 *
 * @param webassemblyBytes A buffer containing the sha1 binary.
 */
exports.instantiateSha1Bytes = async (webassemblyBytes) => {
    const wasm = await bin_1.instantiateRustWasm(webassemblyBytes, './sha1', 'sha1', 'sha1_init', 'sha1_update', 'sha1_final');
    return {
        final: wasm.final,
        hash: wasm.hash,
        init: wasm.init,
        update: wasm.update
    };
};
exports.getEmbeddedSha1Binary = () => utils_1.base64ToBin(bin_1.sha1Base64Bytes).buffer;
/**
 * An ultimately-portable (but slower) version of `instantiateSha1Bytes`
 * which does not require the consumer to provide the sha1 binary buffer.
 */
exports.instantiateSha1 = async () => exports.instantiateSha1Bytes(exports.getEmbeddedSha1Binary());
//# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoic2hhMS5qcyIsInNvdXJjZVJvb3QiOiIiLCJzb3VyY2VzIjpbIi4uLy4uLy4uLy4uL3NyYy9saWIvY3J5cHRvL3NoYTEudHMiXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6Ijs7QUFBQSxvQ0FBZ0Y7QUFDaEYsMENBQTZDO0FBcUQ3Qzs7Ozs7R0FLRztBQUNVLFFBQUEsb0JBQW9CLEdBQUcsS0FBSyxFQUN2QyxnQkFBNkIsRUFDZCxFQUFFO0lBQ2pCLE1BQU0sSUFBSSxHQUFHLE1BQU0seUJBQW1CLENBQ3BDLGdCQUFnQixFQUNoQixRQUFRLEVBQ1IsTUFBTSxFQUNOLFdBQVcsRUFDWCxhQUFhLEVBQ2IsWUFBWSxDQUNiLENBQUM7SUFDRixPQUFPO1FBQ0wsS0FBSyxFQUFFLElBQUksQ0FBQyxLQUFLO1FBQ2pCLElBQUksRUFBRSxJQUFJLENBQUMsSUFBSTtRQUNmLElBQUksRUFBRSxJQUFJLENBQUMsSUFBSTtRQUNmLE1BQU0sRUFBRSxJQUFJLENBQUMsTUFBTTtLQUNwQixDQUFDO0FBQ0osQ0FBQyxDQUFDO0FBRVcsUUFBQSxxQkFBcUIsR0FBRyxHQUFnQixFQUFFLENBQ3JELG1CQUFXLENBQUMscUJBQWUsQ0FBQyxDQUFDLE1BQU0sQ0FBQztBQUV0Qzs7O0dBR0c7QUFDVSxRQUFBLGVBQWUsR0FBRyxLQUFLLElBQW1CLEVBQUUsQ0FDdkQsNEJBQW9CLENBQUMsNkJBQXFCLEVBQUUsQ0FBQyxDQUFDIn0=