"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const bin_1 = require("../bin/bin");
const utils_1 = require("../utils/utils");
/**
 * The most performant way to instantiate sha512 functionality. To avoid
 * using Node.js or DOM-specific APIs, you can use `instantiateSha512`.
 *
 * @param webassemblyBytes A buffer containing the sha512 binary.
 */
exports.instantiateSha512Bytes = async (webassemblyBytes) => {
    const wasm = await bin_1.instantiateRustWasm(webassemblyBytes, './sha512', 'sha512', 'sha512_init', 'sha512_update', 'sha512_final');
    return {
        final: wasm.final,
        hash: wasm.hash,
        init: wasm.init,
        update: wasm.update
    };
};
exports.getEmbeddedSha512Binary = () => utils_1.base64ToBin(bin_1.sha512Base64Bytes).buffer;
/**
 * An ultimately-portable (but slower) version of `instantiateSha512Bytes`
 * which does not require the consumer to provide the sha512 binary buffer.
 */
exports.instantiateSha512 = async () => exports.instantiateSha512Bytes(exports.getEmbeddedSha512Binary());
//# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoic2hhNTEyLmpzIiwic291cmNlUm9vdCI6IiIsInNvdXJjZXMiOlsiLi4vLi4vLi4vLi4vc3JjL2xpYi9jcnlwdG8vc2hhNTEyLnRzIl0sIm5hbWVzIjpbXSwibWFwcGluZ3MiOiI7O0FBQUEsb0NBSW9CO0FBQ3BCLDBDQUE2QztBQXFEN0M7Ozs7O0dBS0c7QUFDVSxRQUFBLHNCQUFzQixHQUFHLEtBQUssRUFDekMsZ0JBQTZCLEVBQ1osRUFBRTtJQUNuQixNQUFNLElBQUksR0FBRyxNQUFNLHlCQUFtQixDQUNwQyxnQkFBZ0IsRUFDaEIsVUFBVSxFQUNWLFFBQVEsRUFDUixhQUFhLEVBQ2IsZUFBZSxFQUNmLGNBQWMsQ0FDZixDQUFDO0lBQ0YsT0FBTztRQUNMLEtBQUssRUFBRSxJQUFJLENBQUMsS0FBSztRQUNqQixJQUFJLEVBQUUsSUFBSSxDQUFDLElBQUk7UUFDZixJQUFJLEVBQUUsSUFBSSxDQUFDLElBQUk7UUFDZixNQUFNLEVBQUUsSUFBSSxDQUFDLE1BQU07S0FDcEIsQ0FBQztBQUNKLENBQUMsQ0FBQztBQUVXLFFBQUEsdUJBQXVCLEdBQUcsR0FBRyxFQUFFLENBQzFDLG1CQUFXLENBQUMsdUJBQWlCLENBQUMsQ0FBQyxNQUFNLENBQUM7QUFFeEM7OztHQUdHO0FBQ1UsUUFBQSxpQkFBaUIsR0FBRyxLQUFLLElBQXFCLEVBQUUsQ0FDM0QsOEJBQXNCLENBQUMsK0JBQXVCLEVBQUUsQ0FBQyxDQUFDIn0=