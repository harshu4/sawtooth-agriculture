"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const bin_1 = require("../bin/bin");
const utils_1 = require("../utils/utils");
/**
 * The most performant way to instantiate ripemd160 functionality. To avoid
 * using Node.js or DOM-specific APIs, you can use `instantiateRipemd160`.
 *
 * @param webassemblyBytes A buffer containing the ripemd160 binary.
 */
exports.instantiateRipemd160Bytes = async (webassemblyBytes) => {
    const wasm = await bin_1.instantiateRustWasm(webassemblyBytes, './ripemd160', 'ripemd160', 'ripemd160_init', 'ripemd160_update', 'ripemd160_final');
    return {
        final: wasm.final,
        hash: wasm.hash,
        init: wasm.init,
        update: wasm.update
    };
};
exports.getEmbeddedRipemd160Binary = () => utils_1.base64ToBin(bin_1.ripemd160Base64Bytes).buffer;
/**
 * An ultimately-portable (but slower) version of `instantiateRipemd160Bytes`
 * which does not require the consumer to provide the ripemd160 binary buffer.
 */
exports.instantiateRipemd160 = async () => exports.instantiateRipemd160Bytes(exports.getEmbeddedRipemd160Binary());
//# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoicmlwZW1kMTYwLmpzIiwic291cmNlUm9vdCI6IiIsInNvdXJjZXMiOlsiLi4vLi4vLi4vLi4vc3JjL2xpYi9jcnlwdG8vcmlwZW1kMTYwLnRzIl0sIm5hbWVzIjpbXSwibWFwcGluZ3MiOiI7O0FBQUEsb0NBSW9CO0FBQ3BCLDBDQUE2QztBQXFEN0M7Ozs7O0dBS0c7QUFDVSxRQUFBLHlCQUF5QixHQUFHLEtBQUssRUFDNUMsZ0JBQTZCLEVBQ1QsRUFBRTtJQUN0QixNQUFNLElBQUksR0FBRyxNQUFNLHlCQUFtQixDQUNwQyxnQkFBZ0IsRUFDaEIsYUFBYSxFQUNiLFdBQVcsRUFDWCxnQkFBZ0IsRUFDaEIsa0JBQWtCLEVBQ2xCLGlCQUFpQixDQUNsQixDQUFDO0lBQ0YsT0FBTztRQUNMLEtBQUssRUFBRSxJQUFJLENBQUMsS0FBSztRQUNqQixJQUFJLEVBQUUsSUFBSSxDQUFDLElBQUk7UUFDZixJQUFJLEVBQUUsSUFBSSxDQUFDLElBQUk7UUFDZixNQUFNLEVBQUUsSUFBSSxDQUFDLE1BQU07S0FDcEIsQ0FBQztBQUNKLENBQUMsQ0FBQztBQUVXLFFBQUEsMEJBQTBCLEdBQUcsR0FBRyxFQUFFLENBQzdDLG1CQUFXLENBQUMsMEJBQW9CLENBQUMsQ0FBQyxNQUFNLENBQUM7QUFFM0M7OztHQUdHO0FBQ1UsUUFBQSxvQkFBb0IsR0FBRyxLQUFLLElBQXdCLEVBQUUsQ0FDakUsaUNBQXlCLENBQUMsa0NBQTBCLEVBQUUsQ0FBQyxDQUFDIn0=